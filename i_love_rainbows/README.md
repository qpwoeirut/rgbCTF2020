# rgbCTF 2020 Writeups: I Love Rainbows
by qpwoeirut

Category: Cryptography (but really should have been in Beginner)<br>
Points: 50<br>
Description: Can you figure out why?<br>
Files: rainbows.txt

## Explanation
The title of the challenge refers to [Rainbow Tables](https://en.wikipedia.org/wiki/Rainbow_table) which are used to decode hashes.
Since the same input into a hash function will always give the same output, values can be pre-calculated into a lookup, or rainbow, table.
Honestly I thought this challenge would be a little harder, but I guess the title was a pretty big giveaway.

There's a script to solve at `solve_rainbows.py`.
If you wanted, you could probably also just search each hash with whatever search engine you prefer.
Of course that would take a bit of time, but it would work.