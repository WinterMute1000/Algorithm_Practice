def union_range(rangeList,range1,range2):
    print(rangeList)
    new_range=[0,0]
    new_range[0]=range1[0] if range1[0]<=range2[0] else range2[0]
    new_range[1]=range1[1] if range1[1]>=range2[1] else range2[1]
    del rangeList[rangeList.index(range1)]
    del rangeList[rangeList.index(range2)]
    rangeList.append(new_range)
    rangeList.sort()

rangeList=[[2,4],[1,5],[7,9]]
rangeList.sort()
isOver=False

while not isOver:
    isOver=True

    for i in range(len(rangeList)-1):
        if rangeList[i][0]<=rangeList[i+1][0] and rangeList[i][1]>=rangeList[i+1][0]:
             union_range(rangeList,rangeList[i],rangeList[i+1])
             isOver=False

        if not isOver:
            break
rangeList.sort()
print(rangeList)

                


