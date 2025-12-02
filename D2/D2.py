with open("input.txt") as file:
    r = [i.split("-") for i in file.readline().rstrip().split(",")]
print(r)