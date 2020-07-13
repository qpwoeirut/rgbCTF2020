"""
Source file for Simple RSA
"""


from sympy import randprime, mod_inverse
from math import gcd


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


p = randprime(1e40, 1e41)
q = randprime(1e8, 1e9)
e = 65537

n = p * q

lmbd = lcm(p - 1, q - 1)
d = mod_inverse(e, lmbd)

message = b"REDACTED"
m = int.from_bytes(message, 'little')
c = pow(m, e, n)

assert pow(c, d, n) == m

print("n =", n)
print("e =", e)
print("c =", c)
