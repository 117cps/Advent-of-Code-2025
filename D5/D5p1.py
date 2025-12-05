FNAME = "input"

total = 0

def checkstate(i): # checks an id (i) against every id range in table
    for r in table:
        if i in range(r[0],r[1]):
            return 1
    return 0

with open(f"D5/{FNAME}.txt") as file:
    lin = [line.rstrip() for line in file.readlines()]
    table = [[int(line.split("-")[0]), int(line.split("-")[1])+1] for line in lin if "-" in line] # turns range input (ex. 1-3) into 2d list of integers (ex. [[1,3]])
    ids = [int(line) for line in lin if not "-" in line and line!=""] #gets full list of ids

for i in ids:
    total+=checkstate(i)

print(total)