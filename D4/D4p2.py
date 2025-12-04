FNAME = "input"
total = 0
totalr=1
    
#checks the accessibility of a specific entry in the input table   
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

#checks the accessibility of every entry in the input using the check(r,c) function
def checkgrid():
    totalr=0
    for r in range(0,len(table)):
        for c in range(0,len(table[r])):
        
            if check(r, c):
                table[r][c]="X"
                totalr+=1
        
        for c in range(0,len(table[r])):
             if table[r][c]=="X":
                 table[r][c]="."
                 
    return totalr
                
#process input
with open(f"D4/{FNAME}.txt") as file:
    table = [[c for c in line.rstrip()] for line in file.readlines()]

#check input and sum each iterations total of accessible/removed paper rolls
while True:
    a = checkgrid()
    if a<=0:
        break
    total+=a
      
print(total)
