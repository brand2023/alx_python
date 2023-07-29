def is_prime(number):
    if number>=1:
        if number%1==0 and number%number==0 and (number%2!=0 or number%3!=0):
            return(True)
    else:
        return(False)
