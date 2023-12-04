infile = open("day3.txt")
matrix = []
nums = "0123456789"
symbols = "/\\/?<>;~^&(*):*#=%&@!$-+="
sum = 0
for line in infile:
    matrix.append(line.strip())
for lineIndex in range(len(matrix)):
    line = matrix[lineIndex]
    index = 0
    while(index<len(line)):
        if(line[index] in nums):
            firstIndex = index
            lastIndex = index
            for i in range(2):
                if(index+1<len(line) and line[index+1] in nums):
                    lastIndex = index+1
                    index+=1
            #check all the indices surrounding the first and last indexes
            adjacent = False
            for y in range(max(0, lineIndex-1), min(len(matrix), lineIndex+2)):
                for x in range(max(0, firstIndex-1), min(len(line), lastIndex+2)):
                    if(matrix[y][x] in symbols):
                        adjacent = True
            if(adjacent):
                if(firstIndex!=lastIndex):
                    sum+=int(matrix[lineIndex][firstIndex:lastIndex+1])
                else:
                    sum+=int(matrix[lineIndex][index])
        index+=1
print(sum)