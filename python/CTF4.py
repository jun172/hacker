import base64
import string

cipher = base64.b64decode("OExHQzhHNg==").decode()

def rot47(s, k):
    res = ""
    for c in s:
        if 33 <= ord(c) <= 126:
            res += chr(33 + ((ord(c)-33 - k) % 94))
        else:
            res += c
    return res

print("=== Brute Force Start ===")
for key in range(1,129):
    step1 = rot47(cipher, key)
    step2 = ''.join(chr(ord(c)^key) for c in step1)
    if step2.isprintable():
        print(f"[key={key}] {step2}")
