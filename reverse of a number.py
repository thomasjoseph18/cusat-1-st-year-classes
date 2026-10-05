num=int(input("Enter the number"))
rev=0
while num>0:
    rem=int(num%10) #converting the variable to integer data type else it gives decimal values
    rev=int(rev*10+rem)
    num=int(num/10)
print("the reverse of the number=",rev)