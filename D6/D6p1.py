import re

FNAME = "sample"
total = 0

with open(f"D6/{FNAME}.txt") as file:
    li = [[i for i in re.split(" +", line.rstrip()) if i!=""] for line in file.readlines()]
    for i in range(0, len(li)):
        for e in range(0,len(li[i])):
            try: 
                li[i][e]=int(li[i][e])
            except:
                pass

for i in range(0,len(li[0])):
    if 

print(li)