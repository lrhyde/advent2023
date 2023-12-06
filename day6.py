infile = open("day6.txt")
def parseNumList(numList):
    newList = []
    for num in numList:
        if(num!=""): 
            newList.append(int(num))
    return newList
def parseStrList(numList):
    newList = ""
    for num in numList:
        if(num!=""): 
            newList+=num
    return newList
timeList = [[]]
distList = [[]]
for line in infile:
    if(line[0]=="T"):
        timeList[0]= int(parseStrList(line.split(" ")[1:]))
    if(line[0]=="D"):
        distList[0]  = int(parseStrList(line.split(" ")[1:]))
successes = []
for i in range(len(timeList)):
    successes.append(0)
    for j in range(timeList[i]):
        if(j*(timeList[i]-j)>distList[i]):
            successes[i]+=1
sum = 1
for i in range(len(timeList)):
    sum*=successes[i]
print(sum)