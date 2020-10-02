#code for bisection theorem

n=int(input("enter number of iterations:"))
l=int(input("enter left boundary:"))
r=int(input("enter right boundary:"))
def eq(x):
    return float((x*x*x)-(5*x)+1)

def sign(x):
    if( x<0 ):
        return 0
    if( x>0 ):
        return 1

for i in range(n):
    a=eq(l)
    b=eq(r)
    m=(l+r)/2
    mid=eq(m)
    if(a*b<0):
        if(sign(a)!=sign(mid)):
            r=m
        if(sign(b)!=sign(mid)):
            l=m
    print(m)



