# rgbCTF 2020 Writeups: Picking Up The Pieces
by qpwoeirut

Category: Misc<br>
Points: 403<br>
Description:<br>
>Can you help me? I had a flag that I bought at the store, but on the way home, I dropped parts of it on some roads!
>Now some roads have strings of text, and I can't tell which are part of my flag.
>I'm very smart and efficient (but somehow not smart or efficient enough to keep my flag), so I know that I took the fastest way from the store back to my house.<br>
>I have a map with a list of all 200000 roads between intersections, and what strings are on them.
>The format of the map is <intersection 1> <intersection 2> <distance> <string on the road>.
>My house is at intersection 1 and the store is at intersection 200000.

Files: map.txt

## Explanation
This was a pretty straightforward shortest-path problem.
The solution I wrote in Python uses Dijkstra, and takes a few seconds to run.
It's in the `test_map` function in `create_shortest_path_map.py`, which also uses the `dijkstra` function.

Apparently some people were able to cheese the problem by just taking the right strings.
Personally I think that would be harder than just writing (or copy-pasting) as dijkstra, but in any case I should have had only one or two character strings.
Honestly I don't know why I didn't since I ended up having to pad the flag with other words around it so people wouldn't just skip over it.