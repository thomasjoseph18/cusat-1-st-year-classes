n=int(input("Enter the number of data in list "))
x=[]
for y in range(0,n):
    x.append(int(input()))
n4=int(input("enter the number to be rotated"))
n1=x.index(n4)
x=x[n1:]+x[:n1]
print(x)