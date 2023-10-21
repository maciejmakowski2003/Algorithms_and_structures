def AP_search(G):
    n=len(G)
    visited=[False for i in range(n)] 
    parent=[None for i in range(n)] 
    d=[0 for i in range(n)]
    low=[0 for i in range(n)]
    AP=[False for i in range(n)]
    time=0 

    def DFSvisit(G,u):
        nonlocal time
        nonlocal visited 
        nonlocal parent
        nonlocal d 
        nonlocal low 
        nonlocal AP

        children=0

        time+=1 
        visited[u]=True 
        low[u]=time 
        d[u]=time

        for v in G[u]:
            if not visited[v]: 
                parent[v]=u
                children+=1 
                DFSvisit(G,v)

                low[u]=min(low[u],low[v])
                
                if children>1 and parent[u]==None:
                    AP[u]=True

                if parent[u]!=None and low[v]>=d[u]:
                    AP[u]=True

            elif v!=parent[u]:
                low[u]=min(low[u],d[v])


    for u in range(n):
        if not visited[u]:
            DFSvisit(G,u)

    for i in range(n):
        if AP[i]:
            print(i)



G=[
    [1,2],
    [0,2,3,4,6],
    [0,1],
    [1,5],
    [1,5],
    [3,4],
    [1]
    ]

AP_search(G)


