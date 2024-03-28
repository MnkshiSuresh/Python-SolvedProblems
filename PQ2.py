# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

n= int(input("enter the number"))
diff=n-17
if diff<0:
    diff=diff*-1
if diff>17:
    print(2*diff)
else:
    print(diff)
