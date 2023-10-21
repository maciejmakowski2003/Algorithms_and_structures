#if exist (a,b,c) such that a+b=c

def f(A,B,C):
    A.sort() 
    B.sort()
    for c in range(len(C)):
        a=0
        b=len(B)-1
        while a<len(A) and b>=0:
            if A[a]+B[b]==C[c]:
                return True 
            if A[a]+B[b]<C[c]:
                a+=1 
            else:
                b-=1

print(f([3,5,1,6],[15,12,14],[3,17]))
