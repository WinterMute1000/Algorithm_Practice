from collections import namedtuple
DayWork=namedtuple("DayWork","time priority")

numOfDays=int(input("Input Days:"))

if numOfDays >15 or numOfDays <1:
    print("Wrong Days.")
    exit()

workList=[]

for works in range(numOfDays):
    time=int(input("Day %d Works Time:"%(works+1)))
    priority=int(input("Day %d Works Priority:"%(works+1)))
    workList.append(DayWork(time,priority))

bestWorksPriority=0

for day in range(numOfDays-1):
    workPriority=0
    dayWork=day
    while dayWork<numOfDays:
        if (dayWork+workList[dayWork].time) < numOfDays:
            print(dayWork)
            workPriority=workPriority+workList[dayWork].priority
            dayWork=(dayWork+workList[dayWork].time)
            print(workPriority)
        

            if bestWorksPriority < workPriority:
                bestWorksPriority=workPriority
        else:
            dayWork=dayWork+1


print("Best Priority is %d"%bestWorksPriority)
        
        
