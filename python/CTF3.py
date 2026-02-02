import base64

encrypted = "cXBzaXVwZg=="

# ROT47（逆回転）
def rot47_rev(data, key):
    out = bytearray()
    for b in data:
        if 33 <= b <= 126:
            out.append(33 + ((b - 33 - key) % 94))
        else:
            out.append(b)
    return bytes(out)

# XOR
def xor_bytes(data, key):
    return bytes(b ^ key for b in data)

# Base64 decode
raw = base64.b64decode(encrypted)

# bit系でありがちな key 候補
keys = [1, 2, 4, 8, 16, 32, 64, 128]

print("=== Decode Start ===")
for k in keys:
    try:
        step1 = rot47_rev(raw, k)
        step2 = xor_bytes(step1, k)
        text = step2.decode("utf-8", errors="ignore")
        print(f"[key={k}] {text}")
    except:
        pass
