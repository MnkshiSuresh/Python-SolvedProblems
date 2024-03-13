# Write a Python function that takes a positive integer and returns the sum of the cube of all positive integers smaller than the specified number.

def cubing(data):
    sum = 0
    for i in range(1,data+1):
        sum = sum + i**3
    return sum    
        

num=int(input("enter the number: "))
result=cubing(num)
print(result)
