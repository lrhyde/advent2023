infile = open("day4.txt")

def parseNumList(numList):
    newList = []
    for num in numList:
        if(num!=""): 
            newList.append(int(num))
    return newList
points = dict()
copies = dict()
sum = 0
for line_full in infile:
    lineNum = int(line_full.split(": ")[0].strip().split(" ")[len(line_full.split(": ")[0].strip().split(" "))-1])
    copies[lineNum]=1
    points[lineNum]=0
    line = line_full.split(": ")[1]
    actualNums = parseNumList(line.split(" | ")[0].strip().split(" "))
    winningNums = parseNumList(line.split(" | ")[1].strip().split(" "))
    totalNums = actualNums + winningNums
    totalSet = set(totalNums)
    points[lineNum] = len(totalNums)-len(totalSet)
for i in range(1, len(points)+1):
    for j in range(i+1, i+1+points[i]):
        copies[j]+=copies[i]
for i in range(1, len(points)+1):
    sum+=copies[i]
print(sum)