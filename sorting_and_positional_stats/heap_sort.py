def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1)//2 

def heapify(T,i,heap_size):
    l=left(i)
    r=right(i) 
    maxi=i

    if l<=heap_size and  T[l]>T[maxi]:
        maxi=l

    if r<=heap_size and T[r]>T[maxi]:
        maxi=r 

    if maxi!=i:
        T[i],T[maxi] = T[maxi],T[i] 
        heapify(T,maxi,heap_size) 

def build_heap(T):
    n=len(T)

    for i in range(parent(n-1),-1,-1):
        heapify(T,i,n-1)


def heap_sort(T):
    n=len(T)
    build_heap(T)
    heap_size=n-1

    for i in range(n-1,0,-1):
        T[0],T[i] = T[i],T[0]
        heap_size-=1
        heapify(T,0,heap_size)



T=[3,2,7,4,5,6,9,8,1]
heap_sort(T)
print(T)