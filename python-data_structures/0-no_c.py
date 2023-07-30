def no_c(my_string):
    chr=my_string
    for i in my_string:
        if i=="c" and i=="C":
            chr.remove("i")
    return(chr)
