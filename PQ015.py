#Python program to print even lengthed words
def evenwords(string):
    s=string.split(" ")
    for i in range (len(s)):
        leng=len(s[i])
        if leng%2==0:
            print(s[i])
        
        
    
     
        
        
string="althaf is my best friend"
evenwords(string)
