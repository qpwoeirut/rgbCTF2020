from hashlib import md5, sha256
from random import choice, randint

flag = "rgbCTF{4lw4ys_us3_s4lt_wh3n_h4shing}"
pieces = ['r', 'g', 'b', 'C', 'TF', '{4', 'lw', '4y', 's_', 'u', 's3', '_s', '4', 'lt', '_', 'w', 'h3', 'n', '_h', '4s', 'h', 'in', 'g', '}']
# i = 0
# while i < len(flag):
#     start = i
#     i += randint(2, 5) // 2
#     pieces.append(flag[start:i])
assert ''.join(pieces) == flag

hash_func = [choice([md5, sha256]) for _ in range(len(pieces))]

for i, c in enumerate(pieces):
    print(hash_func[i](c.encode()).digest().hex())
    print(hash_func[i](c.encode()).digest().hex())
