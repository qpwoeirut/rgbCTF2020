# rgbCTF 2020 Writeups: Adequate Encryption Standard
by qpwoeirut

Category: Cryptography<br>
Points: TBD<br>
Description:<br>
>I wrote my own AES! Can you break it?
>hQWYogqLXUO+rePyWkNlBlaAX47/2dCeLFMLrmPKcYRLYZgFuqRC7EtwX4DRtG31XY4az+yOvJJ/pwWR0/J9gg==

Files: adequate_encryption_standard.py

## Explanation
For this challenge I wrote my own substitution-permutation network with some random sboxes and pboxes.
I'd be interested if anyone actually attacked my implementation of the SP network and got somewhere, since my sboxes and pboxes aren't chosen with anything particular in mind.
But the intended solvepath for this challenge was to rewrite the `expand_key` function.
It's many-to-one, so you don't actually need to brute force every single key.
You can write your own function to generate every possible key of a certain length that `expand_key` would create.
Then use this list and try decoding until you find the right key and get the flag.
For an example of a solver see `solve_adequate_encryption_standard.py`.

This will probably take around 15 minutes of pure computing time.