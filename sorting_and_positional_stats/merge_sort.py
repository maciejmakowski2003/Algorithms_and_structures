def merge(T,p,q,r):
    L=T[p:q+1]
    R=T[q+1:r+1]

    L+=[float('inf')]
    R+=[float('inf')]

    i=0#iterator L
    j=0#iterator R

    for k in range(r-p+1):
        if L[i]<=R[j]:
            T[p+k]=L[i] 
            i+=1

        else:
            T[p+k]=R[j] 
            j+=1

def merge_sort(T,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(T,p,q) 
        merge_sort(T,q+1,r)
        merge(T,p,q,r)

T=[3,2,7,4,5,6,9,8,1]
n=len(T) 
merge_sort(T,0,n-1)
print(T)

