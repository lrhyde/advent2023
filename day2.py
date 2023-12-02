infile = open("day2.txt")

colors = dict()
sum = 0
for line in infile:
    colors["red"] = 0
    colors["green"] = 0
    colors["blue"] = 0
    line2 = line.split(": ")
    lineNumber = int(line2[0].split(" ")[1])
    rounds = line2[1].split(";")
    isValid = True
    for round in rounds:
        round = round.strip()
        units = round.split(",")
        for unit in units:
            u = unit.split(" ")
            unitArr = []
            for unit in u:
                if(unit!=""):
                    unitArr = unitArr + [unit]
            num = int(unitArr[0])
            color = unitArr[1]
            if(num>colors[color]):
                colors[color] = num
    sum+=colors["red"]*colors["green"]*colors["blue"]
print(sum)