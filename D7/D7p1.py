FNAME="input"

total=0

with open(f"D7/{FNAME}.txt") as file:
    table = [[c for c in line.rstrip()] for line in file.readlines()]

def split(r, c): #enter sublist
    total = 0
    if r>0 and table[r][c]=="^" and table[r-1][c]=="|":
        total+=1
        if c>0:
                table[r][c-1]="|"
        if c<len(table[r])-1:
                table[r][c+1]="|"
    return total
    
def extend(r,c):
    if table[r-1][c] in "|S" and table[r][c] != "^" and r>0:
        table[r][c]="|"
            
    
for r in range(0,len(table)):
    for c in range(0,len(table[r])):
        test=table[r][c]
        extend(r,c)
        total+=split(r,c)
        
print(total)