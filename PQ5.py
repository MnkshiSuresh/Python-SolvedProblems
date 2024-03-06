#Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
#Note: Do not use built-in functions

def maximum(datas):
    valuth=datas[0]
    for i in range(len(datas)):
        if datas[i]>=valuth:
            valuth=datas[i]
    return valuth   
    
    
def minimum(datas):
    cheruth=datas[0]
    for i in range(len(datas)):
        if datas[i]<=cheruth:
            cheruth=datas[i]
    return cheruth
    
    
lists=input("enter list of numbers seperated by space: ")
datas=lists.split()
print(maximum(datas))
print(minimum(datas))
