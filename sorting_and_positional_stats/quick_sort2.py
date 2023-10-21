#iterative
def partition(T,p,r):
    x=T[r] 
    i=p-1 

    for j in range(p,r):
        if T[j]<x:
            i+=1;
            T[i],T[j] = T[j],T[i]

    T[i+1],T[r] = T[r],T[i+1]
    return i+1

def quick_sort(T):
    n=len(T)
    stack=[] 
    stack.append((0,n-1)) 

    while len(stack)>0:
        p,r=stack.pop()
        if p<r:
            q=partition(T,p,r) 
            stack.append((p,q-1)) 
            stack.append((q+1,r))

    print(T) 


quick_sort([3,2,7,4,5,6,9,8,1])