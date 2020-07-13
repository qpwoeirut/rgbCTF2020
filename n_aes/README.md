# rgbCTF 2020 Writeups: N-AES
by qpwoeirut

Category: Cryptography<br>
Points: 50<br>
Description: What if I encrypt something with AES multiple times? `nc challenge.rgbsec.xyz 34567`<br>
Files: n_aes.py

## Explanation
The core observation for this challenge is that Python's scoping means that the default argument for `rand_block` will be the same even if you call it multiple times.
As soon as we know this, we can just brute force all seeds and see which one results in a flag.
The solver script is at `solve_n_aes.py`.

### Note
I completely messed up the provided decryption function seeding. The seed in `decrypt` is an integer but in `rand_block` it's a byte.
And for whatever reason the `seed` function has different behavior for `bytes` and `int`.
Fortunately you can solve by just writing your own decrypt, which is also easier to do since each seed byte is the same.