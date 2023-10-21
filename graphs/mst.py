#mst-minimal spanning trees
#G- undirected with weights

from queue import PriorityQueue


def prims(G):
    n = len(G)
    inf = float('inf')
    parents   = [-1] * n
    weights   = [inf] * n
    processed = [False] * n
    pq = PriorityQueue()
    pq.put((0, 0)) 
    
    while not pq.empty():
        u_weight, u = pq.get()

        if processed[u]: continue # Skip a vertex if it was processed before

        # If we remove the vertex from a priority queue this must be a vertex
        # with the lowest weight in a queue so we will mark this vertex as
        # processed because all the future occurrences of this vertex
        # in a priority queue must be skipped

        processed[u] = True

        # Loop over all the u vertex's neighbours and update parents of such
        # vertices which are not processed and their current weight is greater
        # than the u_weight
        for v, weight in G[u]:
            if not processed[v] and weight < weights[v]:
                parents[v] = u
                weights[v] = weight
                pq.put((weight, v))

    return parents, weights


def get_MST(G):
    parents, weights = prims(G)
    n = len(G)
    G = [[] for _ in range(n)]
    for u in range(n):
        if parents[u] >= 0:
            G[parents[u]].append((u, weights[u]))
            G[u].append((parents[u], weights[u]))
    return G





class Node:
    def __init__(self, id_):
        self.id = id_
        self.parent = self
        self.rank = 0  # The upper tree's height limit
        

def find(x):
    # If we have to compress a path as we are not a root of a tree
    if x != x.parent:
        # Point all sobsequent nodes on a path to the root node
        x.parent = find(x.parent)
    # Return the current (updated) parent of the node
    return x.parent


def union(x, y):
    # Find parents of both x and y
    x = find(x)
    y = find(y)
    # Return if x and y are in the same set as there is nothing to do
    if x == y: return
    # Otherwise, link the smaller tree to the larger one
    if x.rank < y.rank:
        x.parent = y
    else:
        y.parent = x
        # If both x and y have the same rank and y was linked to x,
        # we have to increase the rank of x
        if x.rank == y.rank: x.rank += 1
            
            
def make_set(x):
    return Node(x)


def connected(x, y):
    return find(x) == find(y)


def kruskal(G):
    V, E = G
    # Sort all edges by their weights
    E.sort(key=lambda e: e[2])
    # Makeset for each of the vertices
    vert = [make_set(v) for v in V]
    # In a loop pick an edge of the smallest weight
    # and check if we can add this edge to the minimum
    # spanning tree
    result = []
    for edge in E:
        u, v, weight = edge
        if not connected(vert[u], vert[v]):
            union(vert[u], vert[v])
            result.append(edge)
    # Return the resulting array of MST edges
    return result


G=[
    [[1,1],[4,5],[5,8]],
    [[0,1],[2,3]],
    [[1,3],[3,6],[4,4]],
    [[2,6],[4,2]],
    [[0,5],[2,4],[3,2],[5,7]],
    [[0,8],[4,7]]
]

print(prims(G))