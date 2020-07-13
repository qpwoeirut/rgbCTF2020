# rgbCTF 2020 Writeups: Shakespeare Play, Lost (and found!)
by qpwoeirut

Category: Cryptography<br>
Points: TBD<br>
Description: Did you know RGBsec was founded in the 16th century? Our top notch team of RGBsec archaeologists has uncovered this ancient manuscript to prove it. There also were some numbers inscribed beside this manuscript, they might help you. Unfortunately, flag formats hadn't been invented yet, so you will need to enclose the flag in the flag format.<br>
Files: play, some_numbers.txt

Credit to Quintec for creating the program to write the play.

## Explanation
The Shakespeare play looks pretty weird, and doing a little research reveals that there's a Shakespeare Programming Language.
We can then run the `play` file as SPL.
For this kind of stuff [tio.run](https://tio.run/#) can be used.
When we run the play file, we get `VmxSQ2EyTXlVbGhWYTFacFRXMVNVMWxzVW5OTmJHeFpZa1ZPYUdKVldscFZWekExV1Zaa1JtRjZhejA9`.
Base64 decoding a few times gets us `Hint: Book cipher`.
So now we know what the numbers mean.

The book cipher used in this challenge was `<line number>, <column number>`.
This can be figured out by just trying different formats and seeing which ones are in bounds.
Everything was 0-indexed, since I wrote a script to create the book cipher for me.
We can recover the flag with a script as well. For an example you can see `solve_shakespeare.py`.

You didn't necessarily have to run the SPL play in order to solve, but I figured that it would be a little too guessy otherwise.