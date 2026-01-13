#ifndef DNS_FLOOD_H
#define DNS_FLOOD_H
#include "modules/dns_flood.h"

void dns_flood(const char *target_ip, const char *domain, int duration);
void send_dns_query(const char *target_ip, const char *domain);

#endif
