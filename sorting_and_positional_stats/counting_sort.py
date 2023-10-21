#elementy od 0 - k-1

def counting_sort(A,k):
    n=len(T)
    C=[0]*k 
    B=[0]*n 

    for i in range(n):#count
        C[A[i]]+=1 

    for i in range(1,k):#how many elem <= C[i] 
        C[i]=C[i]+C[i-1]

    for i in range(n-1,-1,-1):#from behind to remain stablility
        B[C[A[i]]-1]=A[i] 
        C[A[i]]-=1

    return B
        
T=[2,0,3,1,1,2,3,2]
print(counting_sort(T,4))

