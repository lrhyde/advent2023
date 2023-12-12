infile = open("day11.txt")
galaxies = []
lineNum = 0
numCols = 0
blankCols = []
blankRows = []
for line in infile:
    line = line.strip()
    if(lineNum==0):
        numCols = len(line)
        blankCols = [True for i in range(numCols)]
    galaxyIndices = [i for i in range(numCols) if line[i]=="#"]
    if(len(galaxyIndices)==0):
        blankRows.append(lineNum)
    for xCoord in galaxyIndices:
        galaxies.append((lineNum, xCoord))
        blankCols[xCoord]=False
    lineNum+=1
blankCols = [i for i in range(numCols) if blankCols[i]]
s = 0
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        inTheWay = sum([1 for b in blankCols if (b>min(galaxies[i][1], galaxies[j][1]) and b<max(galaxies[i][1], galaxies[j][1]))])
        inTheWay+=sum([1 for b in blankRows if (b>min(galaxies[i][0], galaxies[j][0]) and b<max(galaxies[i][0], galaxies[j][0]))])
        s+=inTheWay+abs(galaxies[i][0]-galaxies[j][0]) + abs(galaxies[i][1]-galaxies[j][1])
print(s)