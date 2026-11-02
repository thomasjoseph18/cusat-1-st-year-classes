n=int(input("Enter the muber of data"))
x=[]
for y in range(0,n):
    x.append(int(input()))
x.sort()
print(x)
print("the second largest number=",x[n-2])