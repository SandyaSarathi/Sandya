#sandya
n=int(input())
t=n
rev=0
while(t!=0):
  rem=t%10
  t=t//10
  rev=(rev*10)+rem
if rev==n:
  print("yes")
else:
  print("no")
    
