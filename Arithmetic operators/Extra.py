#program to calculate a power m divided by a power n
a,m,n=int(input("Enter a value:")),int(input("Enter m value:")),int(input("Enter n value:"))
res=a**(m-n)
res1=a**m/a**n
print("The value is :{}".format(res))
print("The value is :{}".format(res1))
