def find_bridges(G):
    n=len(G)
    visited=[False for i in range(n)] 
    parent=[None for i in range(n)] 
    d=[0 for i in range(n)]
    low=[0 for i in range(n)]
    result=[] 
    time=0 

    def DFSvisit(G,u):
        nonlocal time
        nonlocal visited 
        nonlocal parent
        nonlocal d
        nonlocal low
        nonlocal result 

        time+=1 

        visited[u]=True
        d[u]=time 
        low[u]=time

        for v in G[u]:
            if not visited[v]: 
                parent[v]=u 
                DFSvisit(G,v)
                low[u]=min(low[u],low[v])

                if low[v]==d[v]:
                    result.append((u,v))
                    

            elif v!=parent[u]:
                low[u]=min(low[u],d[v])
 


    for u in range(n):
        if not visited[u]:
            DFSvisit(G,u)

    print(result)

G=[
    [1,6],
    [0,2],
    [1,3,6],
    [2,4,5],
    [3,5],
    [3,4],
    [0,2,7],
    [6]
    ]

find_bridges(G)