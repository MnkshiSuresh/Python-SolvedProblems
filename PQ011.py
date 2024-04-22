#Write a Python program to print a variable without spaces between values.
#Sample value : x =30
#Expected output : Value of x is "30"


x=int(input("enter the value of x :"))
print("the value of x is \" %i \" " %x)
s=input("enter the value of y and z on a space gap :")
q=s.split()
y=int(q[0])
z=int(q[1])
print("the value of y is \"%i\" and value of z is \"%i\" " %(y,z))
