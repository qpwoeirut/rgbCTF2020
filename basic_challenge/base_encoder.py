"""
Challenge creator for A Basic Challenge
"""

from base64 import b64encode


def str_to_bin(s: str) -> str:
    print("bin")
    return " ".join([bin(ord(c))[2:] for c in s])


def str_to_oct(s: str) -> str:
    print("oct")
    return " ".join([oct(ord(c))[2:] for c in s])


def str_to_hex(s: str) -> str:
    print("hex")
    return " ".join([hex(ord(c))[2:] for c in s])


def str_to_b64(s: str) -> str:
    print("b64")
    return b64encode(s.encode()).decode()


operations = [str_to_oct, str_to_b64, str_to_hex, str_to_bin]

flag = "rgbCTF{c0ngr4ts_0n_b3ing_B4SIC}"
for op in operations:
    flag = op(flag)

# flag = str_to_b64(flag)
with open("basic_chall.txt", 'w') as out:
    print(len(flag))
    out.write(flag)
