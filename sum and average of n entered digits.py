sum=0
num=int(input("enter the number of digits"))
for i in range (1,num+1):
    number=int(input("Enter the number"))
    sum=sum+number
print("sum+",sum)
print("average=",sum/num)