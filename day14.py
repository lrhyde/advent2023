infile = open("day14.txt")
grid = []
def transpose(arr):
    arr2 = []
    for i in range(len(arr[0])):
        row = ""
        for j in range(len(arr)):
            row+=arr[j][i]
        arr2.append(row)
    return arr2
for line in infile:
    grid.append(line.strip())
grid2 = transpose(grid) #transposing because it's easier to work with rows
loadCount = 0
for row in grid2:
    squareIndex = len(row)+1
    countCircles = 0
    for index in range(len(row)):
        if(row[index]=="#"):
            loadCount+=sum([squareIndex-i for i in range(1, countCircles+1)])
            countCircles = 0
            squareIndex = len(row)-index
        if(row[index]=="O"):
            countCircles+=1
    loadCount+=sum([squareIndex-i for i in range(1, countCircles+1)])
print(loadCount)