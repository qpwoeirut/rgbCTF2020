"""
Category: Misc
Description: Can you help me? I had a flag that I bought at the store, but on the way home, I dropped parts of it on some roads! Now some roads have strings of text, and I can't tell which are part of my flag. I'm very smart and efficient (but somehow not smart or efficient enough to keep my flag), so I know that I took the fastest way from the store back to my house. I have a map with a list of all 500000 roads between intersections, and what strings are on them. The format of the map is <intersection 1> <intersection 2> <distance> <string on the road>. My house is at intersection 1 and the store is at intersection 200000.
Download: map.txt
Solution: This can be solved with a shortest-path algorithm that keeps track of the path. Dijkstra with a parent array should work fine.
"""

from random import randint, choices, shuffle
from string import ascii_letters, digits
from queue import PriorityQueue

N = int(2e5)
M = int(2e5)
MAX_DIST = int(1e9)
TEXT_LEN = (4, 5)
D = int(1e4)  # nodes can only connect if their indexes have a difference of D or less

CHARS = ascii_letters + digits + '[]{}_,'
flag = "Eggs,HandSanitizer,Fruit,Soap,Pizza,IceCream,Bleach,Bread,Milk,Politicians,MacAndCheese,ToiletPaper,rgbCTF{1m_b4d_4t_sh0pp1ng},Cookies,Water,Rice,TomBrady,NewcastleUnited,YourSoul"


def gen_edges():
    adj = [dict() for _ in range(N)]
    for _ in range(M):
        u = randint(0, N - 1)
        v = randint(max(0, u - D), min(u + D, N - 1))
        while u == v or v in adj[u]:
            u = randint(0, N - 1)
            v = randint(max(0, u - D), min(u + D, N - 1))

        dist = randint(1, MAX_DIST)
        val = ''.join(choices(CHARS, k=randint(TEXT_LEN[0], TEXT_LEN[1])))
        adj[u][v] = (dist, val)
        adj[v][u] = (dist, val)

    return adj


def dijkstra(adj: list):
    dist = [float('inf') for _ in range(N)]
    parent = [-1 for _ in range(N)]
    pq = PriorityQueue()
    pq.put(0)  # store node, dist as dist * N + node
    dist[0] = 0

    while pq.qsize() > 0:
        state = pq.get()
        cur_dist = state // N
        cur_node = state % N
        if dist[cur_node] < cur_dist:
            continue

        if cur_node == N - 1:
            next_state = pq.get()
            while next_state % N == cur_node:
                if next_state // N == cur_dist:
                    return None
                if pq.qsize() == 0:
                    break
                next_state = pq.get()
            return parent

        for neighbor, dat in adj[cur_node].items():
            if dist[neighbor] > dist[cur_node] + dat[0]:
                dist[neighbor] = dist[cur_node] + dat[0]
                parent[neighbor] = cur_node
                pq.put((dist[neighbor] * N) + neighbor)

    raise RuntimeError("Graph probably isn't connected")


def recover_path(parents: list):
    path = []
    cur = N - 1

    while cur != -1:
        path.append(cur)
        cur = parents[cur]

    path.reverse()
    return path


def split_into_random_chunks(s: str) -> list:
    end = 0
    pieces = []

    while end < len(s):
        start = end
        end += randint(TEXT_LEN[0], TEXT_LEN[1])
        pieces.append(s[start:end])
    return pieces


def place_flag(path, graph):
    pieces = split_into_random_chunks(flag)

    # store is at the end of the path
    for idx in reversed(range(1, len(path))):
        u = path[idx - 1]
        v = path[idx]

        assert v in graph[u]
        assert u in graph[v]
        graph[u][v] = (graph[u][v][0], pieces[-1])
        graph[v][u] = (graph[v][u][0], pieces.pop())
        assert graph[u][v] == graph[v][u]

        if len(pieces) == 0:
            break


def save_to_file(graph: list):
    edges = []
    for u, neighbors in enumerate(graph):
        for v, dat in neighbors.items():
            assert type(dat) == tuple
            if u >= v:
                continue
            edges.append((u + 1, v + 1, dat[0], dat[1]))
    shuffle(edges)
    with open("map.txt", 'w') as file:
        file.write('\n'.join([' '.join(str(item) for item in edge) for edge in edges]))


def test_map(filename):
    adj = [dict() for _ in range(N)]
    with open(filename, 'r') as f:
        for line in f:
            u, v, d, s = line.strip().split()
            u = int(u) - 1
            v = int(v) - 1
            d = int(d)

            assert v not in adj[u]
            assert u not in adj[v]
            adj[u][v] = (d, s)
            adj[v][u] = (d, s)

    parents = dijkstra(adj)
    path = recover_path(parents)

    for i in range(1, len(path)):
        print(adj[path[i]][path[i - 1]][1], end='')


def generate():
    print("started generating graph")
    graph = gen_edges()
    print("generated graph")
    try:
        parent = dijkstra(graph)
    except RuntimeError:
        print("Error in dijkstra, nodes 1 and 200000 probably aren't connected")
        return False

    print("found graph with unique shortest path")
    shortest_path = recover_path(parent)
    if len(shortest_path) < len(flag) // TEXT_LEN[0]:
        print("There aren't enough edges in the shortest path to hold the flag")
        return False
    place_flag(shortest_path, graph)

    save_to_file(graph)
    return True


def main():
    print('*'*100)
    print("Generation of this graph is randomized")
    print("After generation, a bunch of checks are run to ensure the graph works for the challenge")
    print("The shortest path has to exist between nodes 1 and 200000, and be able to hold the flag")
    print("Depending on your luck and hardware, this may take somewhere between a few seconds and a few minutes")
    print('*'*100)
    while generate() is False:
        print("retrying...")


if __name__ == "__main__":
    # main()
    test_map("map.txt")
