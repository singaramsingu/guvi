size=int(input())
l=input().split()
list1=[]
for i in l:
    list1.append(int(i))
s=sum(list1)
print(s//len(list1))
