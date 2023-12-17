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
def enclosedPoints(grid, path):
    #following a clockwise orientation around the shape, anything between the right side of 
    #the oriented wall and the next wall is enclosed
    enclosed = set()
    for i in range(1, len(path)):
        if(path[i][0]==path[i-1][0] and path[i][1]<path[i-1][1]): #same y, traveling left
            #right is up (-y towards ymin)
            coords = (path[i][0]-1, path[i][1])
            while(coords not in path and coords[0]>=0):
                enclosed.add(coords)
                coords = (coords[0]-1, coords[1])
            coords = (path[i-1][0]-1, path[i-1][1])
            while(coords not in path and coords[0]>=0):
                enclosed.add(coords)
                coords = (coords[0]-1, coords[1])
        if(path[i][0]==path[i-1][0] and path[i][1]>path[i-1][1]): #same y, traveling right
            #right is down (+y towards ymax)
            coords = (path[i][0]+1, path[i][1])
            while(coords not in path and coords[0]<=len(grid)):
                enclosed.add(coords)
                coords = (coords[0]+1, coords[1])
            coords = (path[i-1][0]+1, path[i-1][1])
            while(coords not in path and coords[0]<=len(grid)):
                enclosed.add(coords)
                coords = (coords[0]+1, coords[1])
        if(path[i][1]==path[i-1][1] and path[i][0]>path[i-1][0]): #same x, traveling down
            #right is left (-x towards xmin)
            coords = (path[i][0], path[i][1]-1)
            while(coords not in path and coords[1]>=0):
                enclosed.add(coords)
                coords = (coords[0], coords[1]-1)
            coords = (path[i-1][0], path[i-1][1]-1)
            while(coords not in path and coords[1]>=0):
                enclosed.add(coords)
                coords = (coords[0], coords[1]-1)
        if(path[i][1]==path[i-1][1] and path[i][0]<path[i-1][0]): #same x, traveling up
            #right is right (+x towards xmax)
            coords = (path[i][0], path[i][1]+1)
            while(coords not in path and coords[1]<len(grid[0])):
                enclosed.add(coords)
                coords = (coords[0], coords[1]+1)
            coords = (path[i-1][0], path[i-1][1]+1)
            while(coords not in path and coords[1]<len(grid[0])):
                enclosed.add(coords)
                coords = (coords[0], coords[1]+1)

    return list(enclosed)
for line in input:
    grid.append(line.strip())
    if("S" in line):
        startLine = lineNum
    lineNum+=1
startLocation = (startLine, grid[startLine].index("S"))
distCount = 1
location = (startLocation[0], startLocation[1]+1)
prevLocation = startLocation
path = [location]
while(grid[location[0]][location[1]]!="S"):
    newLocation = nextPoint(grid, location, prevLocation)
    prevLocation = location
    location = newLocation
    path.append(location)
    distCount+=1
ep = enclosedPoints(grid, path)
output = open("day10_shaded.txt", "w")
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if((i, j) in path):
            output.write(str(path.index((i, j))%10))
        elif((i, j) in ep):
            output.write("i")
        else:
            output.write("o")
    output.write("\n")
print(len(ep))