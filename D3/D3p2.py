import copy

FNAME = "input"
total=0

with open(f"D3/{FNAME}.txt") as file:
    r = [list(i.rstrip()) for i in file.readlines()]



for i in r:
    sv=""
    tl = copy.deepcopy(i)
    curr = 0
    for x in range(11,-1,-1):
        c = tl[curr:len(tl)-x]
        m = max(c)
        ind = curr + c.index(m)
        val = tl.pop(ind)
        
        sv+=val
        curr = ind
        
    total+=int(sv)

print(f"total: {total}")