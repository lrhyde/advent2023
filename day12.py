infile = open("day12.txt")
preEvaluated = dict()
def evaluate(pattern, nums):
    #print(pattern, nums)
    if((pattern, tuple(nums)) in preEvaluated):
        return preEvaluated[((pattern, tuple(nums)))]
    if("?" not in pattern and "." not in pattern):
        if(len(nums)>1 or len(pattern)!=nums[0]):
            preEvaluated[(pattern, tuple(nums))] = -1
            return -1
        preEvaluated[(pattern, tuple(nums))] = 1
        #print(pattern, nums)
        return 1
    if("?" not in pattern):
        sections = pattern.split(".")
        sections = [s for s in sections if(s!='')]
        if(len(sections)!=len(nums)):
            preEvaluated[(pattern, tuple(nums))]=-1
            #print(pattern, nums)
            return -1
        for i in range(len(sections)):
            if(evaluate(sections[i], [nums[i]])==-1):
                #print(pattern, nums)
                preEvaluated[(pattern, tuple(nums))] = -1
                return -1
        preEvaluated[(pattern, tuple(nums))] = 1
        return 1
    if(len(pattern)<len(nums)-1+sum(nums)):
        #print(pattern, nums)
        preEvaluated[(pattern, tuple(nums))] = -1
        return -1
    qindex = pattern.index("?")
    dot = evaluate(pattern[0:qindex] + "." + pattern[qindex+1:], nums)
    hashtag = evaluate(pattern[0:qindex] + "#" + pattern[qindex+1:], nums)
    if(dot==-1 and hashtag==-1):
        preEvaluated[(pattern, tuple(nums))] = -1
        return -1
    if(dot==-1 or hashtag==-1):
        preEvaluated[(pattern, tuple(nums))] = max(dot, hashtag)
        return max(dot, hashtag)
    if(dot>=0 and hashtag>=0):
        preEvaluated[(pattern, tuple(nums))] = dot + hashtag
        return dot + hashtag
    preEvaluated[(pattern, tuple(nums))] = 1
    return 1
add = 0
for line in infile:
    pattern = line.strip().split(" ")[0]
    pattern = pattern + "?" + pattern + "?" + pattern + "?" + pattern + "?" + pattern
    nums = [int(i) for i in line.strip().split(" ")[1].split(",")]
    nums = nums + nums + nums + nums + nums
    e = evaluate(pattern, nums)
    #print(line, e)
    add+=e
    print("done", line)
print(add)