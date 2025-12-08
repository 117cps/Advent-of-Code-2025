import math

FNAME = "sample"

with open(f"D8/{FNAME}.txt") as file:
    inp = [line.rstrip().split(",") for line in file.readlines()]
    inp = [tuple(list(map(int, line))) for line in inp]


dist = {}
conn = {}
connlist = []
for p in inp:
    dist[p] = {}
    for i in inp:
        if i!=p:
            dist[p][i] = math.dist(p, i)

for p in dist.keys():
    s = min(dist[p], key=dist[p].get)
    conn[p]=s
    dist[p].pop(s)
    dist[s].pop(p)

for p in conn.keys():
    connlist.append([p, conn[p]])

for i in range(len(connlist)-1, -1, -1):
    for x in range(len(connlist)-1, -1, -1):
        if conn[i][0]!=0 and conn[x]!=0 and connlist[i][0] in connlist[x] and i!=x:
            connlist[x].append(connlist[i][1])
            connlist[i]=0
            continue
        elif conn[i][0]!=0 and conn[x]!=0 and connlist[i][1] in connlist[x] and i!=x:
            connlist[x].append(connlist[i][0])
            connlist[i]=0
            continue
print(connlist)

#print(conn)
