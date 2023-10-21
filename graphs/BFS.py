#breadth-first-search O(V+E) dla reprezentacji listowej

from collections import deque

def BFS(G,s):
    n=len(G)
    visited=[False for i in range(n)] 
    parent=[None for i in range(n)] 
    d=[-1 for i in range(n)] 

    Q=deque()

    Q.append(s)
    visited[s]=True 
    d[s]=0

    while len(Q)>0:
        u=Q.popleft() 

        for v in G[u]:
            if not visited[v]:
                visited[v]=True 
                d[v]=d[u]+1 
                parent[v]=u 
                Q.append(v) 

    print(d)


G=[[1,2],[0,4],[0,3,5],[2,4],[1,3,5],[2,4,6],[5,7],[6]]

BFS(G,0)

