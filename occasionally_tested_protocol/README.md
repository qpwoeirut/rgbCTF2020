# rgbCTF 2020 Writeups: Occasionally Tested Protocol
by qpwoeirut

Category: Cryptography<br>
Points: TBD<br>
Description:<br>
But clearly not tested enough... can you get the flag?<br>
`nc challenge.rgbsec.xyz 12345`<br>
Files: otp.py

## Explanation
The premise of this challenge is that it's an unbreakable one-time-pad.
Of course, it's not really unbreakable.
I did intentionally use a lot of one-letter variables and I added `just_a_random_message` as a distraction/hint.
But it's not hard to see that the program just xors the flag with random numbers that it generates.
Then we can notice that the random numbers are seeded with the time.
Once we know this, it's easy to use the same seed and decrypt the one-time-pad.
Script to solve at `solve_otp_seeded_random.py`.

Depending on your network latency, you might also have had issues since your seed will be a little higher.
You can just brute force the last 10 seconds and that should be enough.

## just_a_random_message
The just_a_random_message was meant to serve as a distraction which provided a little hint if you did bother decoding it.
Unfortunately I screwed up and somehow removed the last word, which was "random".
So the hint decodes to `I appreciate that you are reading this. Now solve the challenge! Go! Go! Why are you still reading? Go! This hint is ` and then just stops.
Good thing is that it's not really necessary to solve the challenge.