string=input('Input:')
substr=''
substr_len=0

for i in range(len(string)):
    now_substr=''
    now_substr_len=0
    for j in range(i,len(string)):
        if not string[j] in now_substr:
            now_substr=now_substr+string[j]
            now_substr_len=now_substr_len+1
        else:
            break

    if now_substr_len>substr_len:
        substr=now_substr
        substr_len=now_substr_len


print(substr_len)
print(substr)
