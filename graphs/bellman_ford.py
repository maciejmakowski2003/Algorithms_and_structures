#shortest paths with any w

def bellman_ford(G,s):#O(V*E)
    n=len(G)
    d=[float('inf') for i in range(n)]
    d[s]=0 

    for i in range(n-1):
        for u in G:
            for v,weight in G[u]: 
                if d[u] != float('inf') and d[v] > d[u] + weight:
                    d[v] = d[u] + weight 


    for u in G:#negative weight cycle detect
            for v,weight in G[u]: 
                if d[u] != float('inf') and d[v] > d[u] + weight:
                    print("negative weight cycle")
                    return None

    return d
