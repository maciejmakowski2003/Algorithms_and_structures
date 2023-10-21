def selection_sort(T):
    for i in range(0,len(T)-1):
        mini=i

        for j in range(i+1,len(T)):
            if T[j]<T[mini]:
                mini=j

        T[i],T[mini] = T[mini],T[i]

T=[2,8,1,4,5,6,3]
selection_sort(T) 
print(T)