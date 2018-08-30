import math
t=int(input())
c=0
for i in range(2,int(math.sqrt(t))+1):
    if(t%i==0):
        c=1
if(c==1):
    print("no")
else:
    print("yes")
