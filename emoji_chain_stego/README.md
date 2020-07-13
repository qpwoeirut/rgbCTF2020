# rgbCTF 2020 Writeups: Emoji Chain Stego
by qpwoeirut

Category: Forensics<br>
Points: 500<br>
Description: I was inspired by the incredibly intelligent and nuanced conversations in #cryptography and #forensics to create a new stego technique!<br>
Files: emoji_chain_stego.png (renamed in this repo to failed_emoji_chain_stego.png)

# I messed this up and I'm sorry
I thought I'd get fancy and obfuscate the Python image encoder, which included changing some ints to booleans.
Only problem with that is that I was using numpy arrays, which don't appreciate booleans being used as indexes.
>\>\>\> import numpy as np<br>
>\>\>\> arr = np.array([1,2,3,4,5])<br>
>\>\>\> arr<br>
>array([1, 2, 3, 4, 5])<br>
>\>\>\> arr[0]<br>
>1<br>
>\>\>\> arr[False]<br>
>array([], shape=(0, 5), dtype=int64)

So as a result, the red channel didn't get encoded.
The blue and green channels still were set, since in Python `True + False == 1`.
Again, I'm sorry. I really should have run my full solution after obfuscating, but I only ran the second part.
This is why you test comprehensively!

## Explanation of Intended Solution (which didn't work with the provided file)
You still had to make a mostly guessy leap in order to solve the correct file.
Each emoji has to be extracted out of the image so stego can be done on each separately.
The top emoji, :simp:, was meant to be encoded with this pastebin link: https://pastebin.com/HRFH1Xna.
The intended way to find it was `zsteg -a top_emoji.png`, which would have gotten you the link.
But like I said in the previous section, the red channel wasn't encoded so you can't actually do this with the provided file.

Once you had the pastebin link, you got the encoder for the rest of the :purrlice: emojis.
The encoder factors the char it's trying to encode into ordered pairs of factors.
Then it randomly chooses a pair and adds a Gaussian random to one of the numbers.
Then the lsb at the coordinate this pair represents is set.
It does this 100 times, although some lsbs might get set multiple times, so there aren't really 100 lsbs set.
This isn't that hard to decode - an easy way to do so is to just keep a counter of pairs and adjacent numbers.
We don't even need to weight the counter and it should still be fine.
For the intended solution you can see an example at `solve_emoji_chain_stego.py`.

## The Guess Gods of rgbCTF
2 teams actually managed to solve this even without the source provided.
I guess with enough thinking and trying of random ideas you would eventually come across this, but it's pretty impressive that people were able to blindly figure out the stego technique.
We can probably add this challenge to our list of guessy challenges in rgbCTF 2020.


## Remarks
I'm a little sad and disappointed that I messed this up. I think that, had I executed this correctly, it would have been a nice challenge.
Although you did have to make a leap by separating all the images, it's not that far-out and I believe most teams would have gotten there.
If anyone cares to try solving the fixed challenge file, you can find it at `emoji_chain_stego.png`.
The broken challenge file is at `failed_emoji_chain_stego.png`.