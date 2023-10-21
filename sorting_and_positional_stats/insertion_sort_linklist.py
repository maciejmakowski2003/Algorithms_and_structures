class Node:
    def __init__(self,val,next=None):
        self.next=next 
        self.val=val


def create_list(L):
    g=Node(None)
    p=g

    for el in L:
        p.next=Node(el) 
        p=p.next

    return g

def print_all(p):
    p=p.next
    while p!=None:
        print(p.val)
        p=p.next 


def insert(p,el):
    tail=p
    q=p.next 

    while q!=None and el>q.val:
        tail=q 
        q=q.next

    tail.next=Node(el,q)


def insertion_sort(g):
    sorted=Node(None,None)
    g=g.next

    while g.next!=None:
        p=g.next 
        g.next=g.next.next 
        p.next=None
        insert(g,p.val)

    return sorted


g=create_list([8,7,6,5,4,3,2,1])
g=insertion_sort(g)
print_all(g)



