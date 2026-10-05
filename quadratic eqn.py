import math
a=int(input("enter number a"))
b=int(input("enter number b"))
c=int(input("enter number c"))
d=(b*b)-(4*a*c)
if d==0:
    r1=(-b)/2*a
    print("roots=",r1)
elif d>0:
    r1=(-b+math.sqrt(d))/2*a
    r2=(-b-math.sqrt(d))/2*a
    print("roots=",r1,",",r2)
else:
    print("Roots are imaginary")