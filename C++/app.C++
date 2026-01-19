#include <pcap.h>
#include <iostream>
#include <unordered_map>
#include "json.hpp"  // json.hpp を include
using json = nlohmann::json;

int main(int argc, char** argv){
    if(argc < 2){
        std::cerr << "Usage: " << argv[0] << " <file.pcap>\n";
        return 1;
    }

    const char* fname = argv[1];
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_t* handle = pcap_open_offline(fname, errbuf);
    if(!handle){
        std::cerr << errbuf;
        return 1;
    }

    int total_packets = 0;
    std::unordered_map<std::string,int> ip_count;

    struct pcap_pkthdr* header;
    const u_char* pkt;
    while(pcap_next_ex(handle, &header, &pkt) >= 0){
        total_packets++;
        if(header->len < 34) continue; // Ethernet + IP minimum
        if(pkt[12] != 0x08 || pkt[13] != 0x00) continue; // IPv4 check

        std::string src = std::to_string(pkt[26]) + "." + std::to_string(pkt[27]) + "." +
                          std::to_string(pkt[28]) + "." + std::to_string(pkt[29]);
        ip_count[src]++;
    }

    pcap_close(handle);

    // JSON 出力
    json j;
    j["total_packets"] = total_packets;
    j["top_ips"] = json::array();
    for(auto& kv : ip_count){
        j["top_ips"].push_back({{"ip", kv.first}, {"count", kv.second}});
    }

    std::cout << j.dump(2) << std::endl;
    return 0;
}
