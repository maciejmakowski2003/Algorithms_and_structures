class Employee:
    def __init__(self,fun):
        self.emp = [] 
        self.fun = fun 
        self.f = -1#value of best party root in v
        self.g = -1#wvalue of best party root in v without v


#f(v)= max(v.fun + sum of g(ui),g(v))- ui childern
#g(v)= sum of f(ui) 


def f(v):
    if v.f>=0: return v.f 

    x=v.fun 
    for u in v.emp:
        x+=g(u) 

    y=g(v) 

    v.f=max(x,y) 

    return v.f 

def g(v):
    if v.g>=0: return v.g 

    x=0 
    for u in v.emp:
        x+=f(u)

    v.g=x 

    return v.g
