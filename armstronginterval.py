t=raw_input().split()
num1=int(t[0])
num2=int(t[1])
for i in range(num1+1,num2):
    n=i
    s=0
    while(i>0):
        s=s+((i%10)*(i%10)*(i%10))
        i=i//10
    if s==n:
        print(n),
