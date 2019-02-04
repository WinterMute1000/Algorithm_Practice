def putStone(matrix,list_size):
    last_pattern=0 #마지막으로 놔둔 패턴
    sum=0
    while list_size>=0:
        sum=sum+getPattern(matrix,last_pattern,list_size)
        list_size=list_size-1

    return sum

def getPattern(matrix,last_pattern,list_size):
    pattern_dic={0:getMax(matrix,last_pattern,list_size),
                 1:getNextPattern1(matrix,last_pattern,list_size),
                 2:getNextPattern2(matrix,last_pattern,list_size),
                 3:getNextPattern3(matrix,last_pattern,list_size),
                 4:getNextPattern4(matrix,last_pattern,list_size)}
    return pattern_dic[last_pattern]

def getMax(matrix,last_pattern,list_size):
    now_max=0
    now_pattern=0
    
    for i in range(1,5):
        if now_max<getPatternSum(matrix,i,list_size):
            now_pattern=i
            now_max=getPatternSum(matrix,i,list_size)


    last_pattern=now_pattern
    return now_max

def getNextPattern1(matrix,last_pattern,list_size):
    now_max=0
    now_pattern=0
    
    for i in range(2,4):
        if now_max<getPatternSum(matrix,i,list_size):
            now_pattern=i
            now_max=getPatternSum(matrix,i,list_size)

    last_pattern=now_pattern
    return now_max

def getNextPattern2(matrix,last_pattern,list_size):
    now_max=0
    now_pattern=0
    
    for i in range(1,5):
        if i!=2 and now_max<getPatternSum(matrix,i,list_size):
            now_pattern=i
            now_max=getPatternSum(matrix,i,list_size)

    last_pattern=now_pattern
    return now_max

def getNextPattern3(matrix,last_pattern,list_size):
    now_max=0
    now_pattern=0
    
    for i in range(1,3):
        if now_max<getPatternSum(matrix,i,list_size):
            now_pattern=i
            now_max=getPatternSum(matrix,i,list_size)

    last_pattern=now_pattern
    return now_max
            
def getNextPattern4(matrix,last_pattern,list_size):
    pattern_2_num=getPatternSum(matrix,2,list_size)
    last_pattern=2
    
    return pattern_2_num

def getPatternSum(matrix,pattern,list_size):
     pattern_num={1:matrix[0][list_size],
                 2:matrix[1][list_size],
                 3:matrix[2][list_size],
                 4:matrix[0][list_size]+matrix[2][list_size]}

     return pattern_num[pattern];

    

matrix=[[6,7,12,-5,5,3,11,3],[-8,10,14,9,7,13,8,5],
        [11,12,7,4,8,-2,9,4]]

print(putStone(matrix,7))
