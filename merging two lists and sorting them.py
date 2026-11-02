n=int(input("Enter the number of data in list 1"))
x=[]
for y in range(0,n):
    x.append(int(input()))
n=int(input("Enter the muber of data"))
x2=[]
for y in range(0,n):
    x2.append(int(input()))
x3=x+x2
x3.sort()
print(x3)