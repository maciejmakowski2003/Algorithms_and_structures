#sortowanie link listy uzywajac idei merge_sorta
class Node:
    def __init__(self,val,next=None):
        self.next=next 
        self.val=val 


def l_merge(l1,l2):
    if l1==None:
        return l2 

    if l2==None:
        return l1 

    head,tail=None,None
    while l1!=None and l2!=None:
        if l1.val<l2.val:
            tmp=l1 
            l1=l1.next 

        else:
            tmp=l2
            l2=l2.next 

        if tail==None:
            tail=tmp 
            head=tmp 

        else:
            tail.next=tmp 
            tail=tail.next

        tail.next=None 

    if l1!=None:
        tail.next=l1 

    else:
        tail.next=l2 

    return head 

def n_series(l):
    curr=l 

    while curr.next!=None and curr.val<=curr.next.val:
        curr=curr.next 

    rest=curr.next 
    curr.next=None 

    return l, rest

def merge_sort(l):
    head=l
    while True:
        l,tail=head,None
        head=None
        counter=0 
        
        while l is not None:
            s1,l = n_series(l)
            if l is None and counter==0:
                return s1 

            counter+=1
            if l is None:
                tail.next=s1 
                l=head 
                break

            s2,l = n_series(l)
            merged=l_merge(s1,s2)
            if head is None:
                head=merged
                tail=merged 

            else:
                tail.next=merged 

            while tail.next is not None:
                tail=tail.next

            
