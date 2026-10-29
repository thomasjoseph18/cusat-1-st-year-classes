x=[]
num=int(input("enter the number of digits"))
num1=num-1
print ("enter the numbers")
while num-1>=0:
    no=int(input())
    x.append(no)
    num-=1
greatest=0; smallest=x[num1]
while num1-1>=0:
    x2=x[num1]
    if x2>greatest:
        greatest=x2
    num1-=1
    if x2<smallest:
        smallest=x2
print("the highest no =",greatest)
print("the smallest no =",smallest)