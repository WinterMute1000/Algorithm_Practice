def Solution(num):
    fibo=[0,1]
    index=2
    now=0
    
    while 1:
      now=fibo[index-2]+fibo[index-1]

      if now >=num:
          break
      fibo.append(now)
      index=index+1

    fibo_sum=0
    for i in range(len(fibo)):
        if fibo[i]%2==0:
            fibo_sum=fibo_sum+fibo[i]

    return fibo_sum

if __name__=='__main__':
    num=input('input:')
    print Solution(num) 

