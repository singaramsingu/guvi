t=raw_input().split()
for i in range(int(t[0])+1,int(t[1])):
    if(i%2==0):
        continue
    else:
        print(i),
