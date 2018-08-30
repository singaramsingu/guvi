t=int(input())
n=t
s=0
while(t>0):
    s=s+((t%10)*(t%10)*(t%10))
    t=t//10
if s==n:
    print("yes")
else:
    print("no")
