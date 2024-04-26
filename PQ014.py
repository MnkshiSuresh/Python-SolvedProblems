#Python program to reverse a string
def reverse(string):
    leng=len(string)
    end=leng-1
    rev=""
    while end>=0:
            rev+=string[end]
            end=end-1
            
    print(rev)    
        
    
     
        
        
string="althaf"
reverse(string)
