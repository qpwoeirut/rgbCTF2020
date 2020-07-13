# rgbCTF 2020 Writeups: Ye Old PRNG
by qpwoeirut

Category: Misc<br>
Points: 403<br>
Description: I found a really old prng... can you exploit it? `nc challenge.rgbsec.xyz 23456`<br>

## Explanation
This challenge has an nc server which generates random numbers, and then asks you to generate the next ones.
The main part of this challenge is to figure out how it's generating random numbers.
From the title and description, it's safe to just try old PRNGs and see which one matches.
From Wikipedia's [List of PRNGs](https://en.wikipedia.org/wiki/List_of_random_number_generators), we can just start from the oldest and work our way down.
And it happens that the oldest one is the one we're looking for.

From here just implement the RNG and get the flag.
My implementations can be found at `solve_ye_old_prng.py` and `ye_old_prng.py`.