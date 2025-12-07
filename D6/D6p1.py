import re

FNAME = "input"
total = 0

with open(f"D6/{FNAME}.txt") as file:
    li = [[i for i in re.split(" +", line.rstrip()) if i!=""] for line in file.readlines()]
    for i in range(0, len(li)):
        for e in range(0,len(li[i])):
            try: 
                li[i][e]=int(li[i][e])
            except:
                pass

for c in range(0,len(li[0])): 
    if li[len(li)-1][c]=="+":
        temp = 0
        for r in range(0,len(li)-1):
            temp+=li[r][c]
    elif li[len(li)-1][c]=="*":
        temp = 1
        for r in range(0,len(li)-1):
            temp*=li[r][c]
    total+=temp
    temp=0

        

print(total)