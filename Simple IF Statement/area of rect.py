#Program on Are of Rectangle
#Ex-4
l=float(input("Enter the length of the rectangle: "))
b=float(input("Enter the breadth of the rectangle: "))
if(l>0)and(b>0):
    ar=l*b
    print("*"*40)
    print("Length is:{}".format(l))
    print("Breadth is:{}".format(b))
    print("Area of Rectangle:{}".format(ar))
    print("*"*40)
if(l<=0):
    print("{} is invalid length".format(l))
if(b<=0):
    print("{} is invalid breadth".format(b))
print("Program Execution has been completed")
