total = 0

with open("sample.txt") as file:
    r = [i.split("-") for i in file.readline().rstrip().split(",")]
ids = 0
for i in r:
    ids = [x for x in range(int(i[0]),int(i[1])+1)]
    for i in ids:
        numstr = str(i)
        l = len(numstr)
        if (len(numstr)%2)!=0:
            continue

        if numstr[0]*l==numstr:
            total+=i
            continue



#print(r)