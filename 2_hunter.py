n=int(input())
l=[int(i) for i in input().split()]
l1=[]
for i in range(0,len(l)):
  l1.append(max(l))
  k=l.index(max(l))
  del(l[k])
s=""
for i in l1:
  s=s+str(i)
print(s)
