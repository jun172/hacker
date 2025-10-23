package main

import (
	"context"
	"encoding/csv"
	"flag"
	"fmt"
	"net"
	"os"
	"strings"
	"sync"
	"time"
)

var (
	hostsArg    = flag.String("hosts", "127.0.0.1", "Comma-separated hosts or CIDR (simple single-IP or comma list)")
	portsArg    = flag.String("ports", "80", "Comma-separated ports")
	timeoutArg  = flag.Duration("timeout", 3*time.Second, "Connection timeout")
	concurrency = flag.Int("concurrency", 50, "Max concurrent workers")
	outFile     = flag.String("out", "", "CSV output file (optional)")
	httpProbe   = flag.Bool("http", true, "Send simple HTTP GET to HTTP ports to solicit banners")
	readLimit   = flag.Int("readlimit", 1024, "Max bytes to read from service")
)

type result struct {
	Host   string
	Port   string
	Banner string
	Error  string
}

func parseHosts(hs string) []string {
	parts := strings.Split(hs, ",")
	var out []string
	for _, p := range parts {
		p = strings.TrimSpace(p)
		if p == "" {
			continue
		}
		// Note: for simplicity we accept single IPs only or comma list.
		out = append(out, p)
	}
	return out
}

func parsePorts(ps string) []string {
	parts := strings.Split(ps, ",")
	var out []string
	for _, p := range parts {
		p = strings.TrimSpace(p)
		if p == "" {
			continue
		}
		out = append(out, p)
	}
	return out
}

func probe(ctx context.Context, host, port string, timeout time.Duration, httpProbe bool, readLimit int) result {
	address := net.JoinHostPort(host, port)
	dialer := &net.Dialer{}
	cctx, cancel := context.WithTimeout(ctx, timeout)
	defer cancel()
	conn, err := dialer.DialContext(cctx, "tcp", address)
	if err != nil {
		return result{Host: host, Port: port, Banner: "", Error: err.Error()}
	}
	defer conn.Close()

	conn.SetDeadline(time.Now().Add(timeout))

	// If httpProbe and port looks like 80/8080/8000/etc, send a small GET
	if httpProbe && (port == "80" || port == "8080" || port == "8000" || port == "443") {
		fmt.Fprintf(conn, "GET / HTTP/1.0\r\nHost: %s\r\n\r\n", host)
	}

	// read up to readLimit bytes (non-blocking by deadline)
	buf := make([]byte, readLimit)
	n, err := conn.Read(buf)
	if err != nil && n == 0 {
		// Some services don't send banners; that's ok.
		return result{Host: host, Port: port, Banner: "", Error: ""}
	}
	banner := string(buf[:n])
	// sanitize newlines
	banner = strings.ReplaceAll(banner, "\r\n", "\\n")
	banner = strings.ReplaceAll(banner, "\n", "\\n")
	if len(banner) > 300 {
		banner = banner[:300] + "..."
	}
	return result{Host: host, Port: port, Banner: banner, Error: ""}
}

func worker(ctx context.Context, jobs <-chan [2]string, results chan<- result, wg *sync.WaitGroup) {
	defer wg.Done()
	for job := range jobs {
		host := job[0]
		port := job[1]
		res := probe(ctx, host, port, *timeoutArg, *httpProbe, *readLimit)
		results <- res
	}
}

func main() {
	flag.Parse()

	hosts := parseHosts(*hostsArg)
	ports := parsePorts(*portsArg)

	// build job list
	var jobsList [][2]string
	for _, h := range hosts {
		for _, p := range ports {
			jobsList = append(jobsList, [2]string{h, p})
		}
	}

	jobs := make(chan [2]string, len(jobsList))
	results := make(chan result, len(jobsList))

	ctx := context.Background()
	var wg sync.WaitGroup

	workers := *concurrency
	if workers > len(jobsList) {
		workers = len(jobsList)
	}
	for i := 0; i < workers; i++ {
		wg.Add(1)
		go worker(ctx, jobs, results, &wg)
	}

	go func() {
		for _, job := range jobsList {
			jobs <- job
		}
		close(jobs)
	}()

	// Wait for workers to finish in background
	go func() {
		wg.Wait()
		close(results)
	}()

	// collect
	var all []result
	for r := range results {
		all = append(all, r)
		// print to stdout
		if r.Error != "" {
			fmt.Printf("%s:%s\tERROR: %s\n", r.Host, r.Port, r.Error)
		} else if r.Banner != "" {
			fmt.Printf("%s:%s\tBANNER: %s\n", r.Host, r.Port, r.Banner)
		} else {
			fmt.Printf("%s:%s\t(no banner)\n", r.Host, r.Port)
		}
	}

	// optional CSV output
	if *outFile != "" {
		f, err := os.Create(*outFile)
		if err != nil {
			fmt.Fprintf(os.Stderr, "failed to create output file: %v\n", err)
			return
		}
		defer f.Close()
		w := csv.NewWriter(f)
		w.Write([]string{"host", "port", "banner", "error"})
		for _, x := range all {
			w.Write([]string{x.Host, x.Port, x.Banner, x.Error})
		}
		w.Flush()
		fmt.Printf("results written to %s\n", *outFile)
	}
}
