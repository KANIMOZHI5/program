z=input()
z=z.split()
a=int(z[0])
b=int(z[1])
arr=[]
sum=0
for i in range(0,a):
  x=int(input())
  arr.append(x)
for i in range(0,b):
  sum=sum+arr[i]
print(sum)
  
