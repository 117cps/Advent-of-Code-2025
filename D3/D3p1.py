FNAME = "input"

total=0

with open(f"D3/{FNAME}.txt") as file:
    r = [list(i.rstrip()) for i in file.readlines()]
    print(r)
    #r = [[int(x) for x in r[y]] for y in range(0,len(r)-1)]
print(f"r: {r}")



for i in r:

    
    m1 = i[:(len(i)-1)].index(max(i[:(len(i)-1)])) 
    m2l = i[(m1+1):]
    m2 = m2l.index(max(m2l))
    
    bank=int(str(i[m1])+str(m2l[m2]))
    print(i, f'bank voltage: {bank}')
    total += bank

print(f"total: {total}")