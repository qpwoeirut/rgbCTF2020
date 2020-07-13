# rgbCTF 2020 Writeups: r/ciphers
by qpwoeirut

Category: Beginner<br>
Points: 50<br>
Description: RGBsec does not endorse (or really even know at this point) what the content is on that sub reddit.
(It's just the title of the challenge)<br>
Files: 11.txt

## Explanation
This cipher is a substitution cipher.
We can figure this out through frequency analysis.
See below for an explanation of frequency analysis.
Once we know it's a substitution cipher, we can just plug it into [www.guballa.de/substitution-solver](https://www.guballa.de/substitution-solver) or [www.quipqiup.com](https://quipqiup.com/).
This gets us:
>This is a monoalphabetic substitution cipher, which can be attacked with frequency analysis. Although this attack can be done by hand, it's usually much easier to use a program to do it for you. Two good websites that will decrypt substitution ciphers for you are at guballa.de/substitution-solver and quipqiup.com. If you haven't tried them before, you should check them out. Here's your flag: rgbCTF{just_4sk_th3_int3rn3t_t0_d3crypt_it}
>Also, Alec believes it's very important that you see this: https://i.redd.it/1p7w8k0272851.jpg

## Frequency Analysis
In this section, when I say "substitution cipher" I really mean "monoalphabetic substitution cipher".

Since substitution ciphers only do one-to-one substitution of letters, the frequency of how often letters appear stays the same.
The only difference is that the letters that appear most often are different.
Since we have a long block of text, and we're pretty sure it's English, we can compare how frequently each letter appears and then compare them to the frequency of letters in English.
For an example of a (very simple) program that gets letter frequency you can see `frequency_analyzer.py`.