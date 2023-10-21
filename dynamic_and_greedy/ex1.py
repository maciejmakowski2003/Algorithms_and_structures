# 1.knapsack in O(n*sum(P))
# 2.min cost form (0,0) to (n,n) on chessboard
# 3.min amount of coins to give a change
# 4.whether exist subset of given sum
# 5.LCS
# 6.LIS nlogn
# 7.min cost of matrix multiplication

# 1.
def filter(W,P,B):
    new_W=[] 
    new_P=[] 

    for i in range(len(W)):
        if W[i]<=B:
            new_W.append(W[i]) 
            new_P.append(P[i]) 
            
    return new_W,new_P


def knapsack(w,p,B):
    W,P=filter(w,p,B) 
    n=len(P)
    p_max=sum(P)

    F=[[B+1 for i in range(p_max+1)] for j in range(n)] 

    if W[0]<=B:
        for i in range(P[0]+1):
            F[0][i]=W[0] 
            
    for i in range(1,n):
        for j in range(p_max+1):
            F[i][j] = F[i-1][j] 

            if P[i]>=j:
                if W[i]<F[i-1][j]:
                    F[i][j]=W[i] 

            elif W[i] + F[i-1][j-P[i]]<=B:
                F[i][j]=min(F[i-1][j],W[i] + F[i-1][j-P[i]])

            if F[i][j]>B:
                break
            
    for i in range(p_max,-1,-1):
        if F[n-1][i]<=B: return i

    return 0


P = [5, 3, 8, 4, 1]
W = [60, 50, 115, 70, 5]
B = 115

#print(knapsack(W,P,B))



#2. 


def min_cost(A):
    n=len(A) 

    F=[[0 for i in range(n)] for j in range(n)] 
    F[0][0]=A[0][0]

    for i in range(1,n):
        F[0][i]=F[0][i-1] + A[0][i] 
        F[i][0]=F[i-1][0] + A[i][0] 


    for i in range(1,n):
        for j in range(1,n):
            F[i][j]=min(F[i-1][j],F[i][j-1])+A[i][j] 


    return F[n-1][n-1]

#3.

def coin_exchange(coins,amount):
    counts=[(amount+1) for i in range(amount+1)] 
    counts[0]=0 

    for i in range(1,amount+1):
        for coin in coins:
            if coin<=i:
                counts[i]=min(counts[i],counts[i-coin]+1) 

    return counts[amount] if counts[amount]<=amount else None 

#print(coin_exchange([2, 5],13))

#4.

def if_sum_exist(A,t):
    n=len(A) 

    F=[[False for i in range(t+1)] for j in range(n)]#True- exist sum j for 0-i indexes

    for i in range(n):
        F[i][0]=True 

    if A[0]<t+1: F[0][A[0]]=True 

    for i in range(1,n):
        for j in range(1,t+1):
            if A[i]<=j:
                F[i][j]= F[i-1][j] or F[i-1][j-A[i]] 

            else:
                F[i][j]=F[i-1][j] 


    return F[n-1][t]


#print(if_sum_exist([3, 5, 0, 0, 17, 5, 2, 7, 8],10))
#print(if_sum_exist([3, 5, 0, 0, 17, 5, 2, 7, 8],3))



#5. 

def LCS(N,M):
    n=len(N)
    m=len(M)

    F=[[None for i in range(n+1)] for j in range(m+1)]#F[i][j]


    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                F[i][j]=0 

            elif N[j-1]==M[i-1]:
                F[i][j]=F[i-1][j-1] +1 

            else:
                F[i][j]=max(F[i-1][j],F[i][j-1]) 


    return F[m][n]

print(LCS('aabcaca','abaa'))


# 6. 

def binary_search(A, val):
    left = 0
    right = len(A) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if val > A[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left


def lis(A):
    n=len(A)
    last=[] 


    for i in range(n):
        idx=binary_search(last,A[i]) 

        if idx == len(last): last.append(A[i])
        else: last[idx]=A[i] 


    return len(last)


#print(lis([3, 1, 5, 7, 2, 4, 9, 3, 17, 3]))

#7.

def matrix(A):
    n=len(A)
    dp=[[float('inf') for i in range(n)] for j in range(n)]#F[a][b] min cost of multiplication matrixes from a-b indexes

    for i in range(n):
        dp[i][i]=0
        
    for i in range(n-1):
        dp[i][i+1] = A[i][0]*A[i][1]*A[i+1][1]

    for i in range(n):#beg of interval
        for j in range(n-i):#lenght
            for k in range(i,i+j):
                dp[i][i+j]=min(dp[i][i+j],dp[i][k] + dp[k+1][i+j] + A[i][0]*A[k][1]*A[i+j][1])

    return dp[0][n-1]

A=[(2,3),(3,7),(7,10),(10,4)]

#print(matrix(A))
