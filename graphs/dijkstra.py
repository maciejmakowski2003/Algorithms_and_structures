#shortes path with w>=0

import heapq

#for matrix rep. O(V^2)

def dijkstra(G,s):#O(ElogV)
    n=len(G)
    d=[float('inf') for i in range(n)]
    parent=[None for i in range(n)]
    d[s]=0  

    Q=[]
    heapq.heappush(Q,(d[s],s))

    while Q:
        dist,u = heapq.heappop(Q)

        for v,weight in G[u]:
            if d[v]>d[u]+weight:
                d[v] = d[u]+weight
                parent[v]=u 
                heapq.heappush(Q,(d[v],v))

    return d 

G=[
    [[1,1],[7,2]],
    [[0,1],[2,3],[4,3]],
    [[1,3],[3,5]],
    [[2,5],[4,2],[6,1]],
    [[1,3],[3,2],[5,3],[7,1]],
    [[4,3],[6,8],[8,1]],
    [[3,1],[5,8],[8,4]],
    [[0,2],[4,1],[8,7]],
    [[5,1],[6,4],[7,7]]
]

print(dijkstra(G,0))
