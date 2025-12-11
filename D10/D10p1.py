FNAME = "sample"

with open(f"D10/{FNAME}.txt") as file:
    inp = [[line[ind] for ind in range(0,len(line)-1)] for line in [l.rstrip().split(" ") for l in file.readlines()]]
    schem = [[(1 if c=="#" else 0) for c in list(line[0]) if not c in "[]"] for line in inp]
    lines = [line for line in inp]
    buttonl = [[[int(c) for c in line[ind] if c not in "(),"] for ind in range(1,len(line))] for line in lines]
    buttonbits = [[[1 if x in buttonl[ind][i] else 0 for x in range(0,len(inp[ind][0])-2)] for i in range(0,len(buttonl[ind]))] for ind in range(0,len(inp))]

#(1 if c!="" else 0)
#[0 for x in range(0,len(inp[ind][0])-2)]
    #print(inp)
    #print(inp)
    #print(buttonl)
    print(buttonbits)
    print(buttonl)