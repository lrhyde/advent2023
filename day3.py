infile = open("day3.txt")
matrix = []
nums = "0123456789"
symbols = "/\\/?<>;~^&(*):*#=%&@!$-+="
sum = 0
numslist = []
numsCoords = []
asteriskIndices = []
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
            numslist.append((lineIndex, firstIndex, lastIndex))
            numsCoords.append((lineIndex, firstIndex))
            numsCoords.append((lineIndex, lastIndex))
        if(line[index] == "*"):
            asteriskIndices.append((lineIndex, index))
        index+=1
for asterisk in asteriskIndices:
    numbers = []
    for y in range (max(0, asterisk[0]-1), min(len(matrix), asterisk[0]+2)):
        for x in range(max(0, asterisk[1]-1), min(len(matrix[y]), asterisk[1]+2)):
            if((y, x) in numsCoords):
                ind = numsCoords.index((y, x))
                number1 = 0
                if(ind%2==1):
                    number = numslist[int((ind-1)/2)]
                else:
                    number = numslist[int(ind/2)]
                if(number not in numbers):
                    numbers.append(number)
    if(len(numbers)==2):
        sum+=int(matrix[numbers[0][0]][numbers[0][1]:numbers[0][2]+1])*int(matrix[numbers[1][0]][numbers[1][1]:numbers[1][2]+1])
print(sum)