infile = open("day5.txt")
def parseNumList(numList):
    newList = []
    for num in numList:
        if(num!=""): 
            newList.append(int(num))
    return newList
nums = "0123456789"
list = []
seedList = []
for line in infile:
    if(line.split(" ")[0]=="seeds:"):
        #parse seeds
        seedList = parseNumList(line.split(" ")[1:])
        list.append(seedList)
        ogSeedlist = seedList
    if(line=="\n"):
        list.append([list[len(list)-1][i] for i in range(len(list[len(list)-1]))])
        print(list[len(list)-2])
    elif(line[0] in nums):
        numList = parseNumList(line.split(" "))
        newBounds = (numList[0], numList[0]+numList[2])
        originalBounds = (numList[1], numList[1]+numList[2])
        for i in range(len(list[len(list)-2])):
            if(list[len(list)-2][i]>=originalBounds[0] and list[len(list)-2][i]<originalBounds[1]):
                list[len(list)-1][i] = list[len(list)-2][i]+newBounds[0]-originalBounds[0]
print()
print(min(list[len(list)-1]))