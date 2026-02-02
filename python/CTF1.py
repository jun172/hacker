import base64
import string

# Encrypted Message
enc = "cXBzaXVwZg=="

# Base64 decode
decoded = base64.b64decode(enc)

def rot47(data, key):
    result = bytearray()
    for b in data:
        if 33 <= b <= 126:
            result.append(33 + ((b - 33 + key) % 94))
        else:
            result.append(b)
    return bytes(result)

def xor(data, key):
    return bytes(b ^ key for b in data)

def is_printable(s):
    return all(c in string.printable for c in s)

print("=== Brute Force Start ===")

for key in range(1, 129):  # bits / MB_count 想定範囲
    try:
        step1 = rot47(decoded, key)
        step2 = xor(step1, key)
        text = step2.decode("utf-8")

        if is_printable(text):
            print(f"[key={key}] {text}")

    except:
        continue
