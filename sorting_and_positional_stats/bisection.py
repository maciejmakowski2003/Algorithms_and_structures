import bisect

def bisection_right(T,p,r,x):# T[i]>x
    if p<r:
        q=(p+r)//2
        if T[q]>x:
            return bisection_right(T,p,q,x)

        else:
            return bisection_right(T,q+1,r,x) 

    return p

def bisection_left(T,p,r,x):#index i such as T[i]>=x
    if p<r:
        q=(p+r)//2
        if T[q]<x: 
            return bisection_left(T,q+1,r,x)           

        else:
            return bisection_left(T,p,q,x)

    return p




T=[0,2,5,7,8,9,10,12]
n=len(T)
print(bisection_left(T,0,n-1,3))
print(bisect.bisect_left(T,3))