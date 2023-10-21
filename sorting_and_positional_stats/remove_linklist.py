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


def remove_max(p):
    tail=p 
    q=p.next

    maxi=q.val
    maxi_pointer=q 
    maxi_tail=tail

    while q!=None:
        if q.val>maxi:
            maxi=q.val
            maxi_pointer=q
            maxi_tail=tail
        
        tail=q 
        q=q.next 

    maxi_tail.next=maxi_pointer.next 


g=create_list([1,2,3,4,5,6,8])
remove_max(g)
print_all(g)
