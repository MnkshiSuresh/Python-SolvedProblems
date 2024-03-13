#delete all 3rd number from list

def delete(data):
    if len(data)>=3:
        del data[2]
        return data
    else:
        return data
        
lists=input("enter the numbers seperated by space: ")  
data=lists.split()
print(delete(data))



