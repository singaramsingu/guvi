size=int(input())
l=raw_input().split()
list1=[]
for i in l:
    list1.append(int(i))
list1.sort()
for i in list1:
  print(i),
