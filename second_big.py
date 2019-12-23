int_list=list(map(int,input().split()))
int_list.sort(reverse=True)

if len(int_list)<=1:
    print('Does not exist')
elif len(int_list)==2:
    if int_list[0]==int_list[1]:
        print('Does not exist')
    else:
        print(int_list[1])
else:    
    if int_list[0]==int_list[1] and int_list[1]==int_list[2]:
        print('Does not exist')
    else:
        print(int_list[1])

