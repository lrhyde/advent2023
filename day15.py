infile = open("day15.txt")
inputs = []
def hash(item):
    val = 0
    for char in item:
        val+=ord(char)
        val = (val*17)%256
    return val
for line in infile:
    inputs = line.strip().split(",")
    grid = [[] for i in range(256)]
    for input in inputs:
        if("-" in input):
            label = input[0:input.index("-")]
            box = hash(label)
            for element in grid[box]:
                if(element[0]==label):
                    grid[box].remove(element)
        else:
            label = input[0:input.index("=")]
            box = hash(label)
            found = False
            for e in range(len(grid[box])):
                element = grid[box][e]
                if(element[0]==label):
                    grid[box][e] = (label, int(input[input.index("=")+1:]))
                    found = True
            if(not found):
               grid[box].append((label, int(input[input.index("=")+1:])))
sum = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        sum+=(i+1)*(j+1)*grid[i][j][1]
print(sum)