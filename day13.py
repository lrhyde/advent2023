infile = open("day13.txt")
puzzle = []
sum = 0
def transpose(arr):
    arr2 = []
    for i in range(len(arr[0])):
        row = ""
        for j in range(len(arr)):
            row+=arr[j][i]
        arr2.append(row)
    return arr2

def analyzePuzzle(puzzle):
    for i in range(1, len(puzzle)): #horizontal division
        #i is the divider, where the mirror is
        leftOfDivision = puzzle[0:i]
        rightOfDivision = puzzle[i:len(puzzle)]
        lengthOfDivision = min(i, len(puzzle)-i)
        leftOfDivision = leftOfDivision[(i-lengthOfDivision):i]
        rightOfDivision = rightOfDivision[0:lengthOfDivision]
        rightOfDivision.reverse()
        if(leftOfDivision==rightOfDivision):
            return 100*i
    #reverse to check cols
    puzzle = transpose(puzzle)
    for i in range(1, len(puzzle)): #vertical division
        #i is the divider, where the mirror is
        leftOfDivision = puzzle[0:i]
        rightOfDivision = puzzle[i:len(puzzle)]
        lengthOfDivision = min(i, len(puzzle)-i)
        leftOfDivision = leftOfDivision[(i-lengthOfDivision):i]
        rightOfDivision = rightOfDivision[0:lengthOfDivision]
        rightOfDivision.reverse()
        if(leftOfDivision==rightOfDivision):
            return i

for line in infile:
    line = line.strip()
    if(line!=""):
        puzzle.append(line)
    else:
        sum+=analyzePuzzle(puzzle)
        puzzle = []
sum+=analyzePuzzle(puzzle)
print(sum)