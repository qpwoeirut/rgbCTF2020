# rgbCTF 2020 Writeups: A Fine Day
by qpwoeirut

Category: Beginner<br>
Points: 50<br>
Description:<br>
>It's a fine day to break some ciphers!<br>
>Sujd jd bgxopksbm ljsu tg tqqjgb xjkubo. Tqqjgb xjkubod tob t qvor vq dhidsjshsjvg xjkubo. Jsd nbp xvgdjdsd vq slv ghribod, t tgm i. Sv bgxopks t cbssbo, rhcsjkcp jsd kctxb jg sub tckutibs (dv t=0, i=1, bsx.) ip t, tgm subg tmm i. Qjgtccp stnb suts rvm 26 tgm xvgwbos js itxn jgsv t xutotxsbo.
>Sub tqqjgb xjkubo jdg's obtccp suts dsovgf. Djgxb js'd rvm 26, subob tob vgcp t qbl uhgmobm mjqqbobgs nbpd, lujxu xtg ib btdjcp iohsb qvoxbm. Tgpltp, ubob'd pvho qctf: ofiXSQ{t_qjgb_tqqjgb_xjkubo}<br>

Files: basic_chall.txt

## Explanation
As the title of the challenge suggests, this is an Affine Cipher.
Even if you didn't know that, all ciphers which do some sort of rotation like Caesar and Affine are substitution ciphers.
You can tell whether a cipher is a substitution cipher through frequency analysis, which is a whole other topic I'll talk a bit about in the r/ciphers writeup.
For now, the easiest way to check is to just chuck it into a solver like [www.guballa.de/substitution-solver](https://www.guballa.de/substitution-solver) or [www.quipqiup.com](https://quipqiup.com/).
We had an issue early on where people who did something like this forgot to maintain capitalization, so we made all flag submissions case-insensitive.
But back to our cipher - putting it in a solver gets us:
>This is encrypted with an affine cipher. Affine ciphers are a form of substitution cipher. Its key consists of two numbers, a and b. To encrypt a letter, multiply its place in the alphabet (so a=0, b=1, etc.) by a, and then add b. Finally take that mod 26 and convert it back into a character.
>The affine cipher isn't really that strong. Since it's mod 26, there are only a few hundred different keys, which can be easily brute forced. Anyway, here's your flag: rgbCTF{a_fine_affine_cipher}