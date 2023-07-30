def no_c(my_string):
    for i in my_string:
        if i=="c" and i=="C":
            my_string.remove("i")
    return(my_string)
