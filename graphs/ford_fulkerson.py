#maxiumum flow capacity O(max_flow*E)


from collections import deque

def BFS(G,s,t,parent):
    n=len(G)
    visited=[False for i in range(n)] 
    Q=deque()

    Q.append(s)
    visited[s]=True 

    while len(Q)>0:
        u=Q.popleft() 

        for v in G[u]:
            if not visited[v]:
                visited[v]=True
                parent[v]=u
                Q.append(v) 
                if v==t: return True 

    return False 

def ford_fulkerson(G,sink,source):
    n=len(G)
    parent=[-1 for i in range(n)]

    max_flow=0

    while BFS(G,sink,source,parent):
        path_flow= float("inf") 
        s=sink 

        while(s!=source):
            path_flow=min(max_flow,)


