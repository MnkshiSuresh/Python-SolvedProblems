
#Python program to check whether the string is Symmetrical or Palindrome

def palindrome(string):
    flag=0
    leng=len(string)
    start=0
    end=leng-1
    mid=leng//2
    while start<end:
        if string[start]==string[end]:
            end=end-1
            start=start+1
        else:
            flag=1
            break
            
    if flag==0:
        print("yes palindrome")
        
    else:
        print("no palindrome")
        
        
        
def symmetry(string):
    flag=0
    leng=len(string)
    start=0
    mid=leng//2
    start2=mid
    end=leng-1
    
    while start<mid and start2<end:
        if string[start]==string[start2]:
            start=start+1
            start2=start2+1
        else:
            flag=1
            break
    if flag==1:
        print("not symmetry")
    else:
        print("yes symmetry")
     
        
        
string="mom"
palindrome(string)
symmetry(string)
