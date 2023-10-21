def top_sort(G):
    n=len(G)
    visited=[False for i in range(n)] 
    sorted_list=[None for i in range(n)]
    index=n-1

    def DFSvisit(G,u):
        nonlocal visited 
        nonlocal sorted_list 
        nonlocal index 

        visited[u]=True 

        for v in G[u]:
            if not visited[v]:  
                DFSvisit(G,v) 

        sorted_list[index]=u 
        index-=1

    for u in range(n):
        if not visited[u]:
            DFSvisit(G,u)

    print(sorted_list)



G=[
    [1,2],
    [2,3],
    [4],
    [5],
    [5],
    [6,7],
    [],
    []
        ]

top_sort(G)