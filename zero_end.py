list_num=list(map(int,input().split()))
num_of_zero=0
zero_count=1
first_zero_idx=0
last_zero_idx=0
is_first_zero_search=False
list_len=len(list_num)

list_num.sort(reverse=True)
for i in range(list_len):
    if list_num[i]==0:
        num_of_zero=num_of_zero+1
        if not is_first_zero_search:
            first_zero_idx=i
            last_zero_idx=first_zero_idx
            is_first_zero_search=True
        else:
            last_zero_idx=last_zero_idx+1



if num_of_zero==0 or first_zero_idx==list_len-1:
    print(list_num)

else:
    for i in range(first_zero_idx,last_zero_idx+1):
        list_num[i],list_num[list_len-zero_count]= list_num[list_len-zero_count],list_num[i]
        zero_count=zero_count+1
    print(list_num)


    
