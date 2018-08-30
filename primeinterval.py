import math
t=raw_input().split()
num1=int(t[0])
num2=int(t[1])
for j in range(num1+1,num2):
    c=0
    for i in range(2,int(math.sqrt(j))+1):
        if(j%i==0):
            c=1
    if(c==0):
        print(j),
