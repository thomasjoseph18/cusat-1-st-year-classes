num=int(input("Enter the numbers"))
rev=0
num1=num
while num>0:
    rem=int(num%10) #converting the variable to integer data type else it gives decimal values
    rev=int(rev*10+rem)
    num=int(num/10)
if rev==num1:
    print("the entered no is palindrome")
else:
    print("the entered no is not palindrome")