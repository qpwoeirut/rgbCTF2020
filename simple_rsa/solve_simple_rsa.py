from math import log2, ceil
from sympy import factorint, mod_inverse

n = 5620911691885906751399467870749963159674169260381
e = 65537
c = 1415060907955076984980255543080831671725408472748

factors = factorint(n)
print(factors)

p, q = factors.keys()  # factorint returns a dict, so we need to unpack it
print(p, q)

d = mod_inverse(e, (p - 1) * (q - 1))
decrypted = pow(c, d, p * q)

print(decrypted)

# now we need to convert to letters
print(decrypted.to_bytes(ceil(log2(decrypted) / 8), 'little'))  # we know it's little endian from the source
