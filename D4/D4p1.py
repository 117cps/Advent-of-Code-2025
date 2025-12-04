FNAME = "input"
total = 0

#dirlist = ["tl", "t", "tr", "ml", ]

#def checkspot(dir, r, c):
    
#checks the accessibility of a specific entry in the grid   
def check(r, c):
    dirlist = [[r-1, c-1], [r-1, c], [r-1, c+1], [r,c-1], [r,c+1], [r+1,c-1], [r+1,c], [r+1, c+1]]
    totalr = 0
    
    if table[r][c]!="@":
        return False
                
    for i in dirlist:
        if i[0]<0 or i[1]<0:
            continue
        try:
            if table[i[0]][i[1]]=="@" or table[i[0]][i[1]]=="X":
                totalr+=1
        except:
            continue
        
    if totalr<=3:
        return True
    
    return False
    
                
                
#process input
with open(f"D4/{FNAME}.txt") as file:
    table = [[c for c in line.rstrip()] for line in file.readlines()]
    
#checks the accessibility of every spot in the input using the check(r,c) function
for r in range(0,len(table)):
    for c in range(0,len(table[r])):
        
        if check(r, c):
            table[r][c]="X"
            total+=1
        
print(total)

    
