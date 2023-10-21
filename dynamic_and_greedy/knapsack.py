def knapsack(W,P,B):#O(n*maxW)
    n=len(W)

    f=[[0 for i in range(B+1)] for j in range(n)]
    parent=[None for i in range(n)]

    for b in range(W[0],B+1):
        f[0][b] = P[0] 


    for i in range(1,n):
        for b in range(1,B+1):
            f[i][b]=f[i-1][b]
            parent[i]=i-1

            if b-W[i]>=0:
                f[i][b]=max(f[i-1][b],f[i-1][b-W[i]] + P[i])

    return f[n-1][B]


def get_knapsack(f, W):
    contents = []
    w = len(f[0]) - 1
    for i in range(len(f)-1, 0, -1):
        if f[i][w] != f[i - 1][w]:
            contents.append(i)
            w -= W[i]
    if w >= W[0]: contents.append(0)
    
    return contents
