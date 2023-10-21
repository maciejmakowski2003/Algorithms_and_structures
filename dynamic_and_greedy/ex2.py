#1.Stickler Thief problem
#2.falling bricks
#3.ferry loading- list with lenghts of cars, two lanes of lenght L, how many cars can we fit(order preserved)
#4.knapsack2D

#1.

def maxi(T):
    n=len(T) 

    if n<=2: return max(T) 

    #ai -  max zysk scinajac drzewa od 0,..,i
    dp = [None] * n 
    dp[0] = T[0] 
    dp[1] = max(T[0],T[1])

    for i in range(2,n):
        dp[i] = max(dp[i-1],dp[i-2] + T[i])

    return dp[n-1]


#print(maxi([8, 12, 3, 4, 7, 1, 2, 10]))


#2. 

def check(a,b):
    if a[1]<=b[1] and a[0]>=b[0]:
        return True 

    return False 

def count(T):
    n=len(T)
    dp=[1]*n 

    for i in range(1,n):
        for j in range(i):
            if check(T[i],T[j]):
                dp[i] = max(dp[i],dp[j]+1) 


    return n-max(dp) 

#print(count([(0, 10), (1, 10), (2, 6), (6, 7), (11, 20), (11, 19), (12, 18), (13, 19), (14, 20)]))


#3. 

def adjust(A,L):
    total = 0

    for i in range(len(A)):
        total += A[i] 

        if total > 2*L:
            return i-1 

    return len(A)-1

def ferry(A,L):
    n=len(A)
    last_car_idx = adjust(A,L) 
    dp = [[[None] * (L + 1) for _ in range(L + 1)] for _ in range(last_car_idx+1)] 
    P=['']*n


    def recur(i,l,r):#i-car, l-space on left line, r-space on right line
        if l<0 or r<0: return False  

        if i==0:
            if l >= A[0]: P[0] = 'L'; return True
            if r >= A[0]: P[0] = 'R'; return True
            return False 

        if dp[i][l][r] is None:
            if recur(i - 1, l - A[i], r):
                dp[i][l][r] = True

                P[i] = 'L'
            elif recur(i - 1, l, r - A[i]):
                dp[i][l][r] = True
                P[i] = 'R'

        return dp[i][l][r]


    for i in range(last_car_idx,-1,-1):
        if recur(i,L,L):
            return P

print(ferry([1516, 723, 498, 211, 308, 392, 634, 439, 263, 123488],1824)) 


#4. 

def filter_items(H, W, P, MaxH, MaxW):

    n = len(H)
    H_cp = []
    W_cp = [] 
    P_cp = []
    for i in range(n):
        if 0 < H[i] <= MaxH or 0 < W[i] <= MaxW:
            H_cp.append(H[i])
            W_cp.append(W[i])
            P_cp.append(P[i])
    return H_cp, W_cp , P_cp


def knapsack2D(P,H,W,maxH,maxW): 
    H,W,P = filter_items(H,W,P,maxH,maxW) 
    n=len(P) 

    dp=[[[0]*(maxW+1) for j in range(maxH+1)] for i in range(n)] 

    for h in range(H[0],maxH+1):
        for w in range(W[0],maxW+1):
            dp[0][h][w] = P[0] 

    for i in range(1,n):
        for h in range(1,maxH+1):
            for w in range(1,maxW+1):
                dp[i][h][w] = dp[i-1][h][w] 

                if H[i]<=h and W[i]<=w:
                    dp[i][h][w] = max(dp[i-1][h][w], dp[i-1][h-H[i]][w-W[i]] + P[i])

    return dp[n-1][maxH][maxW] 


#print(knapsack2D([4, 10, 2, 3, 8],[3, 9, 12, 4, 2],[10, 4, 1, 2, 6],20,12))




