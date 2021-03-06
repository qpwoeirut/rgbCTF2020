# COPIED FROM RELEASED SOURCE #

BLOCK_SIZE = 8
ROUNDS = 8

sbox = [111, 161, 71, 136, 68, 69, 31, 0, 145, 237, 169, 115, 16, 20, 22, 82, 138, 183, 232, 95, 244, 163, 64, 229, 224, 104, 231, 61, 121, 152, 97, 50, 74, 96, 247, 144, 194, 86, 186, 234, 99, 122, 46, 18, 215, 168, 173, 188, 41, 243, 219, 203, 141, 21, 171, 57, 116, 178, 233, 210, 184, 253, 151, 48, 206, 250, 133, 44, 59, 147, 137, 66, 52, 75, 187, 129, 225, 209, 191, 92, 238, 127, 241, 25, 160, 9, 170, 13, 157, 45, 205, 196, 28, 146, 142, 150, 17, 39, 24, 80, 118, 6, 32, 93, 11, 216, 220, 100, 85, 112, 222, 226, 126, 197, 180, 34, 182, 37, 148, 70, 78, 201, 236, 81, 62, 42, 193, 67, 8, 164, 43, 252, 166, 221, 208, 176, 235, 149, 109, 63, 103, 223, 65, 56, 140, 255, 218, 54, 153, 2, 228, 1, 240, 248, 246, 110, 156, 60, 227, 207, 254, 51, 174, 79, 128, 155, 251, 242, 177, 135, 230, 154, 179, 15, 189, 143, 130, 27, 107, 211, 30, 105, 19, 134, 124, 125, 245, 76, 204, 12, 26, 38, 40, 131, 117, 87, 114, 213, 212, 102, 195, 101, 55, 10, 47, 120, 200, 217, 88, 83, 36, 198, 249, 192, 23, 94, 181, 73, 185, 172, 165, 58, 53, 202, 106, 5, 7, 175, 89, 72, 90, 14, 162, 158, 119, 139, 77, 108, 190, 91, 29, 49, 159, 33, 113, 214, 4, 123, 199, 167, 35, 239, 84, 3, 132, 98]
pbox = [39, 20, 18, 62, 4, 60, 19, 43, 33, 6, 51, 61, 40, 35, 47, 16, 23, 58, 31, 53, 28, 55, 54, 30, 17, 42, 34, 45, 49, 13, 46, 0, 26, 2, 8, 3, 11, 48, 63, 36, 37, 7, 32, 5, 27, 59, 29, 44, 14, 56, 21, 22, 12, 52, 57, 41, 10, 1, 24, 38, 50, 15, 9, 25]


def pad(block):
    return block + chr(BLOCK_SIZE - len(block)).encode() * (BLOCK_SIZE - len(block))


def to_blocks(in_bytes: bytes) -> list:
    return [in_bytes[i:i + BLOCK_SIZE] for i in range(0, len(in_bytes), BLOCK_SIZE)]


def enc_sub(in_bytes: bytes) -> bytes:
    return bytes([sbox[b] for b in in_bytes])


def enc_perm(in_bytes: bytes) -> bytes:
    num = int.from_bytes(in_bytes, 'big')
    binary = bin(num)[2:].rjust(BLOCK_SIZE * 8, '0')
    permuted = ''.join([binary[pbox[i]] for i in range(BLOCK_SIZE * 8)])
    out = bytes([int(permuted[i:i + 8], 2) for i in range(0, BLOCK_SIZE * 8, 8)])
    return out


def expand_key(key: bytes, key_len: int) -> bytes:
    expanded = bytearray()
    cur = 0
    for byte in key:
        cur = (cur + byte) & ((1 << 8) - 1)
    expanded.append(cur)
    for num in [key[i % len(key)] * 2 for i in range(key_len)]:
        cur = pow(cur, num, 256)
        expanded.append(cur)
    return bytes(expanded)


def encrypt(plain: bytes, key: bytes) -> bytes:
    blocks = to_blocks(plain)
    out = bytearray()
    key = expand_key(key, len(blocks))
    for idx, block in enumerate(blocks):
        block = pad(block)
        assert len(block) == BLOCK_SIZE
        for _ in range(ROUNDS):
            block = enc_sub(block)
            block = enc_perm(block)
            block = bytearray(block)
            for i in range(len(block)):
                block[i] ^= key[idx]
        out.extend(block)
    return bytes(out)


# SOLVER CODE STARTS HERE #
from base64 import b64decode
from time import time


inv_sbox = [sbox.index(i) for i in range(256)]
inv_pbox = [pbox.index(i) for i in range(BLOCK_SIZE * 8)]


def unpad(block):
    pad_len = block[-1]
    if len(block) >= pad_len and len(set(block[-pad_len:])) == 1:
        return block[:-pad_len]
    return block


def dec_sub(in_bytes: bytes) -> bytes:
    return bytes([inv_sbox[b] for b in in_bytes])


def dec_perm(in_bytes: bytes) -> bytes:
    num = int.from_bytes(in_bytes, 'big')
    binary = bin(num)[2:].rjust(BLOCK_SIZE * 8, '0')
    permuted = ''.join([binary[inv_pbox[i]] for i in range(BLOCK_SIZE * 8)])
    out = bytes([int(permuted[i:i + 8], 2) for i in range(0, BLOCK_SIZE * 8, 8)])
    return out


def decrypt(enc: bytes, key: bytes, expand=True) -> bytes:
    blocks = to_blocks(enc)
    out = bytearray()
    if expand:
        key = expand_key(key, len(blocks))
    else:
        assert len(key) >= len(blocks), key
    for idx, block in enumerate(blocks):
        assert len(block) == BLOCK_SIZE
        for _ in range(ROUNDS):
            block = bytearray(block)
            for i in range(len(block)):
                block[i] ^= key[idx]
            block = dec_perm(block)
            block = dec_sub(block)
        out.extend(unpad(block))
    return bytes(out)


def all_expanded_keys(key_len):
    start = time()
    keys = []
    cur_keys = [bytes([i]) for i in range(256)]
    while len(cur_keys) > 0:
        key = cur_keys.pop()
        if len(key) == key_len:
            keys.append(key)
            continue

        # print(key)
        new_keys = set()
        for i in range(0, 512, 2):
            new_keys.add(key + bytes([pow(key[-1], i, 256)]))
        cur_keys.extend(new_keys)
    keys.sort()
    print("Key generation took", time() - start, "seconds")
    return keys


def save_keys(key_len):
    ekeys = all_expanded_keys(key_len)
    with open(f"expanded_keys{key_len}.dat", "wb") as key_list:
        key_list.write(b''.join(ekeys))


def solve(encrypted, key_len):
    try:
        with open(f"expanded_keys{key_len}.dat", "rb") as key_file:
            keys = key_file.read()
    except FileNotFoundError:
        save_keys(key_len)
        with open(f"expanded_keys{key_len}.dat", "rb") as key_file:
            keys = key_file.read()

    assert len(keys) % key_len == 0
    print("There are", len(keys) // key_len, "keys")

    start = time()
    for i in range(0, len(keys), key_len):
        key = keys[i:i + key_len]
        # print(key)
        dec = decrypt(encrypted, key, False)
        if dec.startswith(b"rgbCTF{") and dec.isascii():
            print(key)
            print(dec)
    print("Key enumeration took", time() - start, "seconds")


def main():
    enc = b64decode("hQWYogqLXUO+rePyWkNlBlaAX47/2dCeLFMLrmPKcYRLYZgFuqRC7EtwX4DRtG31XY4az+yOvJJ/pwWR0/J9gg==")
    print("Enc:", enc)
    key_len = len(to_blocks(enc))
    solve(enc, key_len)


if __name__ == '__main__':
    main()
