infile = open("day1.txt")
nums = "123456789"
nums2 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0
for line in infile:
    firstNum = -1
    lastNum = -1
    for i in range(len(line)):
        if(line[i] in nums): 
            if(firstNum==-1):
                firstNum=int(line[i])
            lastNum = int(line[i])
        for j in range(2, 6):
            if(i+j<=len(line) and line[i:i+j] in nums2 ):
                if(firstNum==-1):
                    firstNum=nums2.index(line[i:i+j])
                lastNum = nums2.index(line[i:i+j])
    total = firstNum*10 + lastNum
    sum+=total
print(sum)