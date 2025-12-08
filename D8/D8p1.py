import math

FNAME = "sample"

with open(f"D8/{FNAME}.txt") as file:
    inp = [line.rstrip().split(",") for line in file.readlines()]
    inp = [tuple(list(map(int, line))) for line in inp]


dist = {}
conn = {}

for p in inp:
    dist[p] = {}
    for i in inp:
        if i!=p:
            dist[p][i] = math.dist(p, i)



test = (162, 817, 812)
conn[test] = min(dist[test], key=dist[test].get)
print(conn)

#print(conn)