import re
import copy

FNAME = "input"
total = 0

with open(f"D6/{FNAME}.txt") as file:
    li = [[i for i in x if i!="" and i!="\n"] for x in [line for line in file.readlines()]]

temp=[]  
for c in range(0,len(li[0])):
    t=[]
    for r in range(0,len(li)):
        t.append(li[r][c])
    temp.append(t)

prl = []
tn=[]
opl = []

for i in temp:
    if all(t==" " for t in i):
            prl.append(tn)
            tn=[]
            continue
    n=""
    for e in i:
        if e not in " *+":
            n+=e
        elif e in "*+":
             opl.append(e)
    tn.append(n)
prl.append(tn)    


prl = [list(map(int, line)) for line in prl]

for i in range(0,len(prl)):
    if opl[i]=="*":
        out = 1
        for n in prl[i]:
            out*=n
        total+=out
    elif opl[i]=="+":
        out=0
        for n in prl[i]:
            out+=n
        total+=out
        
print(total)