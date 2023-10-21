def insertion_sort(T,p,r):
    for i in range(p+1,r):
        x=i 
        y=i-1 
        while y>=p and T[x]<T[y]:
            T[x],T[y] =T[y],T[x] 
            x-=1 
            y-=1

def magic_fives(T,p,r):
    if len(T)==1:
        return T[0]

    A=[] 
    for i in range(p,r+1,5):
        if i>r-5:
            insertion_sort(T,i,r)
            A.append(T[(r+i)//2])
        else:
            insertion_sort(T,i,i+5)
            A.append(T[i+2])

        n=len(A)

    return magic_fives(A,0,n-1)

def partition(T,p,r):
    pivot=magic_fives(T,p,r)
    for i in range(p,r+1):
        if T[i]==pivot:
            index=i 

    T[r],T[index] = T[index],T[r]
    x=T[r] 
    i=p-1 

    for j in range(p,r):
        if T[j]<=x:
            i+=1
            T[i],T[j] = T[j],T[i] 

    T[r],T[i+1] = T[i+1],T[r] 

    return i+1


def quick_select(T, l, r, k):#k- smallest

    if (k > 0 and k <= r - l + 1):
  
        q = partition(T, l, r)
  
        if (q - l == k - 1): return T[q]
   
        if (q - l > k - 1):
            return quick_select(T, l, q - 1, k)
   
        return quick_select(T, q + 1, r, k-q+l-1)

T=[10,9,8,7,6,3,4,9,11]
print(quick_select(T,0,8,1))

