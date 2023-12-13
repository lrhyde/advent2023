infile = open("day9.txt")
sum = 0
def parseNumList(numList):
    newList = []
    for num in numList:
        if(num!=""): 
            newList.append(int(num))
    return newList
def extrapolate(sequence):
    complete = False
    differences = []
    differences.append(sequence)
    while(not complete):
        differences.append([differences[len(differences)-1][i+1]-differences[len(differences)-1][i] for i in range(len(differences[len(differences)-1])-1)])
        if(differences[len(differences)-1] == [0 for n in differences[len(differences)-1]]):
            complete = True
    prevDiff = 0
    for i in range(len(differences)):
        iReverse = len(differences)-i-1
        value = differences[iReverse][0] - prevDiff
        prevDiff = value
    return value
for line in infile:
    numLine = parseNumList(line.split(" "))
    ex = extrapolate(numLine)
    sum+=ex
print(sum)