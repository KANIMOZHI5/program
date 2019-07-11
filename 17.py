a=int(input())
b=a
c=0
while(a>0):
  e=a%10
  c=c+e**3
  a=a//10
if (b==c):
  print("yes")
else:
  print("no")
