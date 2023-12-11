infile = open("day7.txt")
bids = []
cardOrder = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
sum = 0
def evalCard(card):
    sCard = list(set(card))
    vals = []
    for c in sCard:
        vals.append(card.count(c))
    vals = sorted(vals)
    vals.reverse()
    score = vals[0]*(14**6)
    if(len(vals)>1):
        score+=vals[1]*(14**5)
    for i in range(len(card)):
        score+=(14**(4-i)) * (13-cardOrder.index(card[i]))
    return score
for line in infile:
    bids.append((evalCard(line.split(" ")[0]), int(line.split(" ")[1]), line.split(" ")[0]))
bids.sort()
sum = 0
for b in range(len(bids)):
    sum+=(b+1)*bids[b][1]
print(sum)