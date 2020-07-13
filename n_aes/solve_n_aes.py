from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from pwn import remote, process
from random import randint, seed

BLOCK_SIZE = 16


def try_seed(enc, key_seed):
    seed(key_seed)
    key = bytes([randint(0, 255) for _ in range(BLOCK_SIZE)])

    enc = b64decode(enc)
    for i in range(128):
        enc = AES.new(key, AES.MODE_ECB).decrypt(enc)

    try:
        enc = unpad(enc, BLOCK_SIZE)
        if enc.isascii():
            return enc
    except ValueError:
        pass
    return None


def main():
    rem = process(["python3", "n_aes.py"])

    enc = rem.recvline().strip()
    print(enc)

    dec = None
    for key in range(256):
        dec = try_seed(enc, bytes([key]))
        if dec:
            break

    assert dec is not None

    rem.recvuntil("> ")
    rem.sendline('3')
    rem.sendline(b64encode(dec))
    rem.sendline('4')
    print(rem.recvall(2).decode())


if __name__ == '__main__':
    main()
