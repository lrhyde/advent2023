infile = open("day19.txt")
workflows = dict()
partArr = []
xmas = "xmas"
for line in infile:
    if(line!='\n' and line[0]!='{'):
        parts = line.split("{")
        name = parts[0]
        rules = parts[1].strip()[0:len(parts[1].strip())-1].split(",")
        newRules = []
        for rule in rules:
            if(':' not in rule):
                newRules.append([rule])
            else:
                r1 = 0
                r2 = "eq"
                r3 = 0
                r4 = "nowhere"
                if("<" in rule):
                    r1 = rule[0:rule.index("<")]
                    r3 = int(rule[rule.index("<")+1:rule.index(":")])
                    r4 = rule[rule.index(":")+1:]
                    r2="<"
                else:
                    r1 = rule[0:rule.index(">")]
                    r3 = int(rule[rule.index(">")+1:rule.index(":")])
                    r4 = rule[rule.index(":")+1:]
                    r2=">"
                newRules.append((r1, r2, r3, r4))
        workflows[name] = newRules
    elif(line!="\n"):
        line = line.strip()[1:len(line.strip())-1]
        components = line.split(",")
        comp = []
        for component in components:
            comp.append(int(component[2:]))
        partArr.append(comp)
total = 0
for comp in partArr:
    currentFlow = "in"
    while(currentFlow!="A" and currentFlow!="R"):
        assigned = False
        for rule in workflows[currentFlow]:
            if(not assigned):
                if(len(rule)==1):
                    currentFlow = rule[0]
                    assigned = True
                else:
                    if(rule[1]=="<" and comp[xmas.index(rule[0])]<rule[2]):
                        currentFlow = rule[3]
                        assigned = True
                    if(rule[1]==">" and comp[xmas.index(rule[0])]>rule[2]):
                        currentFlow = rule[3]
                        assigned = True
            else:
                break
    if(currentFlow=="A"):
        total+=sum(comp)
print(total)