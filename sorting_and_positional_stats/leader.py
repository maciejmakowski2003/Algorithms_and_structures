def find(T):
    n=len(T)
    x=1
    leader=T[0] 

    for i in range(1,n):
        if x>0:
            if T[i]==leader:
                x+=1 

            else:
                x-=1

        else:
            x+=1
            leader=T[i] 

    if x>0:
        count=0
        for i in range(n):
            if T[i]==leader:
                count+=1
        if count>n//2:
            return True 
        
    return False 

print(find([1,2,1,2,1,4,1]))
#then check if leader variable is a real leader of array


