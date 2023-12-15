infile = open("day15.txt")
inputs = []
def hash(item):
    val = 0
    for char in item:
        val+=ord(char)
        val = (val*17)%256
    return val
for line in infile:
    inputs = line.strip().split(",")
    print(sum([hash(input) for input in inputs]))