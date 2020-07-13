from PIL import Image as I
from random import choice as ch, randint as ra
import numpy as n
from secret import V, W, X, Y, Z, flag
def arr(filename):
    i=n.array(I.open(filename),dtype=n.uint8)
    r,g,b=i.shape
    for a in range(r):
        for b in range(g):
            for j in range(3):
                i[a][b][j]|=True
                i[a][b][j]-=True
    I.fromarray(i).save(filename)
def gee(l):
    i=n.array(I.open("f.png"))
    r=127
    g=127
    b=False
    for char in l:
        for bit in bin(ord(char))[2:].rjust(8, '0'):
            bit=int(bit)
            i[r][g][int(b)]|=bit  # THIS WAS THE PROBLEM - NEVER USE BOOLEANS AS INDEXES FOR NUMPY ARRAYS
            b+=True
            if b==3:
                b=False
                g-=True
                if g==-1:
                    g=127
                    r-=True
    return i
def bee(c):
    return[(a,c//a) for a in range(True,c+True) if c%a==False]
def sek(out, m):
    i=n.array(I.open(out))
    s=bee(ord(m))
    b=2
    for _ in range(Z):
        while True:
            r,g = ch(s)
            if ra(False, True)==False:
                r+=n.random.normal(scale=16)
                if r<False or r>=128:continue
            else:
                g+=n.random.normal(scale=16)
                if g<False or g>=128:continue
            r = int(r)
            g = int(g)
            i[r][g][b]|=True
            break
    return i
def I_LOVE_EMOJI_STEGO():
    arr("c.png");arr("f.png");m = [gee("https://pastebin.com/HRFH1Xna")]
    for char in flag: m.append(sek("c.png", char))
    q=n.zeros((((W+V+V)*(len(flag)+True)),W+V+V,4),dtype=n.uint8);q.fill(255);b=3
    for r in range((W+V+V)*(len(flag)+True)):
        for g in range(W+V+V):q[r][g][b] = 0
    for r, i in enumerate(range(V,(W+V+V)*(len(flag)+True),W+V+V)):
        for g in range(W):
            for b in range(W):q[i+g][b+V]=m[r][g][b]
    I.fromarray(q).save("emoji_chain_stego.png")
I_LOVE_EMOJI_STEGO()