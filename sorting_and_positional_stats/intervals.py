#find interval which contains max amount of intervals(find number of intervals)
def fct1(x,y):
    if x[0]>y[0]:
        return True

    return False

def fct2(x,y):
    if x[1]>y[1]:
        return True

    return False


def partition(T,p,r,fct):
    pivot=T[r] 
    i=p-1 

    for j in range(p,r):
        if fct(pivot,T[j]):
            i+=1 
            T[i],T[j] = T[j],T[i]

    T[i+1],T[r] = T[r],T[i+1]

    return i+1

def quick_sort(T,p,r,fct):
    if p<r:
        q=partition(T,p,r,fct)
        quick_sort(T,p,q-1,fct) 
        quick_sort(T,q+1,r,fct)

def depth(L):
    n=len(L)
    low=L 
    high=L.copy()

    low.sort(key=lambda x: x[0])
    high.sort(key=lambda x: x[1])
    #quick_sort(low,0,n-1,fct1) 
    #quick_sort(high,0,n-1,fct2)
    b=high[n-1][1]

    f=[0 for i in range(b+1)]
    g=f.copy()

    amount=0
    for i in range(n):
        g[high[i][1]]=i+1

    for i in range(n-1):
        amount+=1 
        if low[i+1][0]==low[i][0]:
            continue 
        f[low[i+1][0]]=amount

    level=0

    for x in L:
        level=max(level,g[x[1]]-f[x[0]]-1)

    return level