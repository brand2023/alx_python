def is_prime(number):
    for i in range(2,number):
        if number>1:
            if number%i==0:
                return(False)
            else:
                return(True)
        else:
            return(False)
