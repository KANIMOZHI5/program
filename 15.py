a,b=map(int,input().split())
c=a+1
d=[]
for i in range(c,b):
  if c%2==0:
    d.append(c)
  c=c+1
print(*d)
