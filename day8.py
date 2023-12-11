infile = open("day8.txt")
lineNum = 0
directions = ""
nodes = dict()
for line in infile:
    if(lineNum==0):
        directions = line.strip()
    elif(lineNum>=2):
        node = line.split(" = ")[0]
        ln = line.split(" = ")[1].split(", ")[0][1:]
        rn = line.split(" = ")[1].split(", ")[1]
        rn = rn[0:rn.index(")")]
        nodes[node] = (ln, rn)
    lineNum+=1
curr_node = "AAA"
steps = 0
while(curr_node!="ZZZ"):
    index = steps%len(directions)
    if(directions[index]=="L"):
        curr_node = nodes[curr_node][0]
    else:
        curr_node = nodes[curr_node][1]
    steps+=1
print(steps)