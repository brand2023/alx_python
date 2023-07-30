def no_c(my_string):
    chr=my_string
    for i in len(chr):
        if chr[i]=="c" or chr[i]=="C":
            chr[i]=""
    return(chr)
