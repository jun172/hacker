import asyncio
import netifaces
import psutil
from ping3 import ping
import aiohttp

#ネットワーク情報取得
def get_network_info():
    print("[ネットワーク情報取得]")
    for ifase in netifaces.interfaces():
        addrs = netifaces.ifaddresses(ifase)
        if netifaces.AF_INET in addrs:
            for addr in addrs[netifaces.AF_INET]:
                print(f"{ifase} : {addr['addr']}")
#疎通確認            
def cheak_ping(host="8.8.8.8"):
    print("疎通確認")
    result = ping(host, timeout=2)
    return result is not None

# 非同期HTTP通信
async def async_http():
    print("[非同期HTTP通信開始]")
    async with aiohttp.ClientSession() as session:
        async with session.get("https://example.com") as res:
            print("HTTP sratus:", res.status)
            
#通信量監視
def monitor_traffic(threshold=10_000_000):
    print("通信量監視")
    net = psutil.net_io_counters()
    total = net.bytes_sent + net.bytes_recv
    print("通信量:", total)
    return total > threshold

# メインフロー
async def main():
    print("起動")
    
    get_network_info()
    
    if not cheak_ping():
        print("⚠ 通信NG → 警告")
        return 
    else:
        print("✅ 通信OK")
        
    await async_http() 
    
    if monitor_traffic():
        print("🚨 異常検知 → アラート")
    else:
        print("✅ 正常 → 継続")
    
asyncio.run(main())