n=50
ans=0

with open("D1/input.txt") as file:
    rot=[[line[0],line[1:]] for line in file]
    
for ln in rot:
    dir=ln[0]
    amt = int(ln[1])
    if dir=="R":    
        for x in range(0,amt):
            n+=1
            if n==100:
                n=0
                ans+=1 
    elif dir == "L":
        for x in range(0,amt):
            n-=1
            if n==-1:
                n=99
            elif n==0:
                ans+=1
                
print(ans)