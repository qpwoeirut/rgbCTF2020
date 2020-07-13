# rgbCTF 2020 Writeups: [another witty algo challenge name]
by BobbaTea, qpwoeirut

Category: Misc<br>
Points: 409<br>
Description:<br>
>This is pretty simple. You get a list of 5000 by 5000 grid of ones and zeros, and you have to print the number of islands in the grid.<br>
>An island is a collections of ones where each one is adjacent to another one in the island. For a cell to be adjacent to another cell, they must share an edge.<br>
>Submit the number wrapped in the flag format, like rgbCTF{123}

Files: grid.txt

This challenge was released at the beginning of the second day of the CTF.

## Explanation
Like the description says, this is pretty simple.
Although I messed up the description so that it doesn't allow for one-cell islands, I think (or at least hope) most people got it.
Once we get past that stuff, it's just a simple floodfill.
I wrote an answer in C++ in a few minutes using DFS.
You can see it at `islands_chall/solve_islands.cpp`.