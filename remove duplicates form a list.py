x=[]
num=int(input("enter the number of digits"))
num1=num-1
print ("enter the numbers")
while num-1>=0:
    no=int(input())
    x.append(no)
    num-=1
o=[]
for x1 in x:
    if x1 not in o:
        o.append(x1)
    num1-=1
print(o)