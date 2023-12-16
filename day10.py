input = open("day10.txt")
lineNum = 0
startLine = -1
grid = []
def nextPoint(grid, coords, prevCoords):
    #is this the most efficient way to do this? who knows
    if(grid[coords[0]][coords[1]]=="|"):
        return (coords[0]+(coords[0]-prevCoords[0]), coords[1])
    if(grid[coords[0]][coords[1]]=="-"):
        return (coords[0], coords[1]+(coords[1]-prevCoords[1]))
    if(grid[coords[0]][coords[1]]=="J"):
        if(coords[1]==prevCoords[1]):
            return(coords[0], coords[1]-1)
        else:
            return(coords[0]-1, coords[1])
    if(grid[coords[0]][coords[1]]=="L"):
        if(coords[1]==prevCoords[1]):
            return(coords[0], coords[1]+1)
        else:
            return(coords[0]-1, coords[1])
    if(grid[coords[0]][coords[1]]=="F"):
        if(coords[1]==prevCoords[1]):
            return(coords[0], coords[1]+1)
        else:
            return(coords[0]+1, coords[1])
    if(grid[coords[0]][coords[1]]=="7"):
        if(coords[1]==prevCoords[1]):
            return(coords[0], coords[1]-1)
        else:
            return(coords[0]+1, coords[1])
for line in input:
    grid.append(line.strip())
    if("S" in line):
        startLine = lineNum
    lineNum+=1
startLocation = (startLine, grid[startLine].index("S"))
distCount = 1
location = (startLocation[0], startLocation[1]+1)
print(startLocation)
print(location)
prevLocation = startLocation
while(grid[location[0]][location[1]]!="S"):
    newLocation = nextPoint(grid, location, prevLocation)
    prevLocation = location
    location = newLocation
    print(location)
    distCount+=1
print(distCount/2)

