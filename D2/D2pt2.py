import re

total = 0

with open("D2/input.txt") as file:
    r = [i.split("-") for i in file.readline().rstrip().split(",")]
ids = 0
for i in r:
    ids = [int(x) for x in range(int(i[0]),int(i[1])+1)]
    for i in ids:

        numstr = str(i)
        l = len(numstr)

        for y in range(1,(l//2)+1):
            if l % y != 0:
                continue
            segmentlist = re.findall(fr'.{{{y}}}', numstr)
            if len(set(segmentlist))==1:
                total+=i
                break
                
            
print(total)

