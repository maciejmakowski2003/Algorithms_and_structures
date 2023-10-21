def parent(i): return (i-1)//2
def left(i): return 2*i + 1 
def right(i): return 2*i + 2

def heapify(T,i):
    p=parent(i)
    if i!=0 and T[i]>T[p]:
        T[i],T[p] = T[p],T[i] 
        heapify(T,p)

def insert(T,el):
    n=len(T)
    T.append(el)    
    heapify(T,n)

 