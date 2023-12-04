infile = open("day4.txt")

def parseNumList(numList):
    newList = []
    for num in numList:
        if(num!=""): 
            newList.append(int(num))
    return newList

sum = 0
for line in infile:
    line = line.split(": ")[1]
    actualNums = parseNumList(line.split(" | ")[0].strip().split(" "))
    winningNums = parseNumList(line.split(" | ")[1].strip().split(" "))
    totalNums = actualNums + winningNums
    totalSet = set(totalNums)
    if(len(totalNums)!=len(totalSet)):
        sum+=2**((len(totalNums)-len(totalSet))-1)
print(sum)