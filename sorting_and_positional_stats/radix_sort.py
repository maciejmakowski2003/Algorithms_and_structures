def counting_sort(A,k,pos):
    n=len(A)
    C=[0]*k 
    B=[0]*n 

    for i in range(n):#count
        C[ord(A[i][pos])-97]+=1 

    for i in range(1,k):#how many elem <= C[i] 
        C[i]=C[i]+C[i-1]

    for i in range(n-1,-1,-1):#from behind to remain stablility
        B[C[ord(A[i][pos])-97]-1]=A[i] 
        C[ord(A[i][pos])-97]-=1

    return B

def radix_sort(T,d):#d- lenght of words

    for i in range(d-1,-1,-1):
        T=counting_sort(T,26,i)

    print(T) 

T=["kra","art","kot","kit","ati","kil"]
radix_sort(T,3)





