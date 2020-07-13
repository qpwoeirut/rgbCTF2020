# rgbCTF 2020 Writeups: A Basic Challenge
by qpwoeirut

Category: Beginner<br>
Points: 50<br>
Description: This is a nice and basic challenge.<br>
Files: basic_chall.txt

## (Probably Too) Detailed Explanation
We're given a file with binary numbers, separated by spaces.
We know these are binary numbers because they consist of only ones and zeros.
For whatever reason the `From Binary` function in CyberChef fails to decode these, most likely because the numbers aren't padded.
Another easy solution would be to use Python.
We can convert numbers from binary with `int(binary_number, 2)`.
This gives us a bunch of ascii character codes, which we can convert to characters.
These characters turn out to be hex numbers, which we can again decode using the same process.
The only thing we have to change is to use `int(hex_number, 16)`.
Converting these numbers into letters, we get a string of base64 text.
We'll import the Python base64 library to decode this.
Finally, we get a string of octal numbers.
This was probably the part that the most people might have had issues with, since octal isn't that common.
We can tell it's octal because none of the numbers have an 8 or a 9.

The script I used to test this challenge is in `base_decoder.py`.
We go in order from smallest to largest base since a number like 100110 could be interpreted as hex or octal, but is much more likely to be binary.
Obviously since I wrote the challenge I had prior knowledge for writing the script, but each of these steps can be figured out.
Just print your decoded string after each step and take the time to manually figure out what encoding it's in.