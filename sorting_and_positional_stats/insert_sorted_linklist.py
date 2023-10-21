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

g=create_list([1,2,3,4,5,6,8])
insert(g,7)
print_all(g)
