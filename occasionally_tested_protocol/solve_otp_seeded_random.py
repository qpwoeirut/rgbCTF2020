from math import ceil, log2
from random import seed, randint
from pwn import process
from time import time, sleep


def decode_hint():
    text = """
s = 73
t = 479105856333166071017569
_ = 1952540788
s = 7696249
o = 6648417
m = 29113321535923570
e = 199504783476
_ = 7827278
r = 435778514803
a = 6645876
n = 157708668092092650711139
d = 2191175
o = 2191175
m = 7956567
_ = 6648417
m = 7696249
e = 465675318387
s = 4568741745925383538
s = 2191175
a = 1936287828
g = 1953393000
e = 29545
"""
    nums = [int(s.split('=')[1]) for s in text.split('\n') if s]  # get the number from each line
    hint = ""
    for num in nums:
        hint += num.to_bytes(ceil(log2(num) / 8), 'little').decode() + ' '  # convert to string
    return hint


while time() - int(time()) > 0.1:  # give ourselves the greatest chance of getting the same seed
    sleep(0.1)
rem = process(["python3", "otp_seeded_random.py"])  # replace this with nc to solve the actuall chall
seed(int(time()))  # emulate the seeding
rem.recvline()
for _ in range(10):
    assert randint(5, 10000) == int(rem.recvline())  # generate 10 random numbers, just like the server script

b = bytearray([randint(0, 255) for _ in range(40)])  # generate the same randoms for decryption
flag_enc = int(rem.recvline().decode().split(': ')[1])
flag_bytes = flag_enc.to_bytes(40, 'little')
print(''.join([chr(l ^ p) for l, p in zip(flag_bytes, b)]))  # decrypt and print the flag

rem.close()

# decode_hint()
