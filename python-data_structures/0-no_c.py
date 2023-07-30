def no_c(my_string):
    chr=my_string
    for i in range(len(chr)):
        if chr[i]=="c" or chr[i]=="C":
            del chr[i]
    return(chr)
