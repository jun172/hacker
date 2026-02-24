import dns.resolver

def resolve(domain):
    try:
        answers = dns.resolver.resolve(domain,'A')
        for rdata in answers:
            print("IP:", rdata)
    except:
        pass

resolve("exampe.com")