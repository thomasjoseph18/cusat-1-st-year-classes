n=int(input("Enter the number of data in list "))
x=[]
counteven=0
countodd=0
for y in range(0,n):
    x.append(int(input()))
for y1 in range(0,n):
    if x[y1]%2==0:
        counteven+=1
    else:
        countodd+=1
print("the number of even digits=",counteven)
print("the number of odd digits=",countodd)