def isPalindrome(A):
    values=[]
    current=A
    while current:
        values.append(current.data)
        current=current.next
        
    i,j=0,len(values)-1
    while i<j:
        if values[i]!=values[j]:
            return False
        i+=1
        j-=1
    return True