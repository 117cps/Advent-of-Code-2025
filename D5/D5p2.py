import copy

FNAME = "input"

total = 0

with open(f"D5/{FNAME}.txt") as file:
    table = [[int(line.rstrip().split("-")[0]), int(line.rstrip().split("-")[1])] for line in file.readlines() if "-" in line]


table.sort(key=lambda item: item[0]) #sort table by starting value of each range

m=[] #list to hold fully simplified/merged values
c=table[0] # "current" range being tested; set to the first value in table to start

for item in table[1:]: # loop through each range in the table barring the first
    
    if item[0]<=c[1]+1: # checks for the ranges overlapping
        temp=c[0]
        c[1]=max(c[1],item[1]) #simplifies two overlapping ranges; max to make sure that the right value is used (ex. [1,10] & [3,4] would produce an incorrect value otherwise)
        c[0]=temp
    else: 
        m.append(c)
        c=copy.deepcopy(item)
                
m.append(c)

for x in m:
    total+=(x[1]-x[0])+1
    
print(total) 