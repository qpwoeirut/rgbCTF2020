# rgbCTF 2020 Writeups: Simple RSA
by qpwoeirut

Category: Beginner<br>
Points: 50<br>
Description: Can you find a way to attack this RSA implementation?<br>
Files: simple_rsa.txt, simple_rsa.py
Hint: What's the simplest attack against RSA?

## Explanation
The simplest attack on RSA is just to factor `n`.
If we look at the source, we can see that `p` is at most 1e9.
Since this is so small, we can just try all possible values of `p`.
If this is does naively through Python, it will take a few minutes.
But we can use `sympy.factorint` to speed things up a little, so that it will only take a few seconds.
From here, since we have the factors of `p` and `q`, we can calculate the private key and decrypt the message.
See `solve_simple_rsa.py` for an implementation of the solution.