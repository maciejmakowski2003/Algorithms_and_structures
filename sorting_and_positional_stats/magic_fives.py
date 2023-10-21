def insertion_sort(T,p,r):
    for i in range(p+1,r):
        x=i 
        y=i-1 
        while y>=p and T[x]<T[y]:
            T[x],T[y] =T[y],T[x] 
            x-=1 
            y-=1

def magic_fives(T):
    n=len(T)
    if len(T)==1:
        return T[0]

    A=[] 
    for i in range(0,n-1,5):
        if i>n-5:
            insertion_sort(T,i,n)
            A.append(T[(n-1+i)//2])
        else:
            insertion_sort(T,i,i+5)
            print(T)
            A.append(T[i+2])

    return magic_fives(A) 


print(magic_fives([40,12,45,32,33,1,22]))


