t=[]
def fibonacci_sequence(n):
    for i in range(n):
        t[i]=t[i-1]+t[i-2]
    return(t)