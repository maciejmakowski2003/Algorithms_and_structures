#elements are part of {0,..,m-1}
#find smallest missing

def find_smallest(T,p,r):
   if r<p:
       return r+1

   if T[p]!=p:
       return p

   else:
       q=(p+r)//2

       if T[q]>q:
           return find_smallest(T,p,q)

       else:
           return find_smallest(T,q+1,r)

T=[0,2,3,4,5,6,7,8]
n=len(T)
print(find_smallest(T,0,n-1))