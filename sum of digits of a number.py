num=int(input("Enter the number"))
sum=0
while num>0:
    quo=int(num%10)
    sum=sum+quo
    num=num/10
print("SUM OF DGITS=",sum)