#Write a Python function to check whether a number is divisible by another number. Accept two integer values from the user.

def function(a,b):
    if a%b==0:
        return "yes"
    else:
        return "no"
        
print("enter 2 nos to check divisibility:")
a=int(input("1st no:"))
b=int(input("2nd no:"))
print(function(a,b))
