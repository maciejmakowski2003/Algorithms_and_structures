#bitonic version 


def tsp(D):
    n=len(D)
    F=[[float('inf')]*n for i in range(n)]
    F[0][1] = D[0][1] 

    def tspf(i,j,D):
        nonlocal F 

        if F[i][j]!= float('inf'): return F[i][j] 

        if i == j-1:
            best = float('inf') 

            for k in range(j-1):
                best = min(best,tspf(k,j-1,D) + D[k][j]) 

            F[i][j] = best 

        else:
            F[i][j] = tspf(i,j-1,D) + D[j-1][j] 

        return F[i][j]
