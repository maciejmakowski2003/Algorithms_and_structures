#depth-first-search O(V+E) for list rep. 

def DFS(G):
    n=len(G)
    visited=[False for i in range(n)] 
    parent=[None for i in range(n)] 
    time=0 

    def DFSvisit(G,u):
        nonlocal time
        nonlocal visited 
        nonlocal parent

        
        visited[u]=True 

        for v in G[u]:
            if not visited[v]: 
                parent[v]=u 
                DFSvisit(G,v) 

        time+=1 


    for u in range(n):
        if not visited[u]:
            DFSvisit(G,u)

    print(time)





G=[[1,2],[0,4],[0,3,5],[2,4],[1,3,5],[2,4,6],[5,7],[6]]

DFS(G)