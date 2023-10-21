#longest icreasing subsequence O(n^2)

def LIS(A):
    n=len(A) 

    f=[1 for i in range(n)]
    parent=[-1 for i in range(n)]

    for i in range(1,n):
        for j in range(i):
            if A[i]>A[j] and f[j]+1>f[i]:
                f[i] = f[j]+1
                parent[i]=j

    return max(A)