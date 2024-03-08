def mergesort(a,l,h):
    if l<h:
        m=l+(h-1)//2
        mergesort(a,l,m)
        mergesort(a,m+1,h)
        combine(a,l,m,h)
def combine(a,l,m,h):
    n1=m-l+1