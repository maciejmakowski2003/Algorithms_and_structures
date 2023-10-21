def DFS(G):
    n=len(G)
    visited=[False for i in range(n)] 
    d=[0 for i in range(n)]
    time=0 

    def DFSvisit(G,u):
        nonlocal time
        nonlocal visited 

        time+=1
        d[u]=(time,u)
        visited[u]=True 

        for v in G[u]:
            if not visited[v]:  
                DFSvisit(G,v) 


    for u in range(n):
        if not visited[u]:
            DFSvisit(G,u)

    return d

def DFS2(G,d):
    n=len(G)
    visited=[False for i in range(n)] 
    component=[]
    components=[]

    def DFSvisit(G,u):
        nonlocal visited 
        nonlocal component

        visited[u]=True 

        for v in G[u]:
            if not visited[v]: 
                DFSvisit(G,v)
                
        component.append(u)


    for u in d:
        if not visited[u[1]]:
            DFSvisit(G,u[1])
            components+=[component]
            component=[]

    return components

    



def find_strongly_connected_components(G):
    n=len(G)
    d=DFS(G)
    d.sort()
    print(d)
    
    H=[[] for i in range(n)]

    for i in range(n):
        for j in G[i]:
            H[j].append(i)


    components=DFS2(H,d)

    print(components)

G=[
    [1],
    [2],
    [0,4],
    [4],
    [5],
    [6],
    [3]
    ]

find_strongly_connected_components(G)

