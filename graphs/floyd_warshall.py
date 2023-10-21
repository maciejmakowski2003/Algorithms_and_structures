#shortest paths contains {v1,...,vk} knowing {v1,...,vk-1} O(V^3)

def floyd_warshall(G):
    n=len(G)
    dist=[[G[i][j] for j in range(n)] for i in range(n)]
    parent=[[None for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j]!=float("inf"):parent[i][j]=i

    for t in range(0,n):
        for u in range(n):
            for v in range(n):
                dist[u][v]=min(dist[u][v],dist[u][t]+dist[t][v])

    return dist

