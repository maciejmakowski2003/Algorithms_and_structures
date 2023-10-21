#without tail rec
def partition(T,p,r):
    x=T[r] 
    i=p-1 

    for j in range(p,r):
        if T[j]<x:
            i+=1;
            T[i],T[j] = T[j],T[i]

    T[i+1],T[r] = T[r],T[i+1]
    return i+1


def quick_sort(T,p,r):
    while p<r:
        q=partition(T,p,r) 
        quick_sort(T,p,q-1) 
        p=q+1 #quick_sort(T,q+1,r)