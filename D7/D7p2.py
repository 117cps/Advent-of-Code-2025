FNAME="input"

with open(f"D7/{FNAME}.txt") as file:
    table = [[c for c in line.rstrip()] for line in file.readlines()]     
    
mem = [[None for i in e] for e in table]
    
def step(r,c):
    if r>=(len(table)):
        return 1
    
    if table[r][c]=="^":
        if mem[r][c-1] is not None and mem[r][c+1] is not None:
            return mem[r][c-1] + mem[r][c+1]
        else:
            mem[r][c-1] = step(r,c-1)
            mem[r][c+1] = step(r,c+1)
            return mem[r][c-1] + mem[r][c+1] 
    else:
        mem[r][c] = step(r+1,c)
        return mem[r][c]

print(step(1,table[0].index("S")))