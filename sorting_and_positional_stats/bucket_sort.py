def bucket_sort(T):
    n=len(T)
    A=[[] for i in range(n)]#bucket0 <0,1/n) 
        
    for i in range(n):
        A[int(T[i]*n)].append(T[i])

    for bucket in A:
        bucket.sort()

    i=0 

    for bucket in A:
        for el in bucket:
            T[i]=el 
            i+=1


T=[0.24,0.51,0.10,0.55]
bucket_sort(T)
print(T)