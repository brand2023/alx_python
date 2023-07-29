t=[]
def fibonacci_sequence(n):
    if n>0:
        for i in range(n):
            t[i]=t[i-1]+t[i-2]
            return(t)
    else:
        return(t)