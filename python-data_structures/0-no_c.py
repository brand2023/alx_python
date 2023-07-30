def no_c(my_string):
    chr=my_string
    for i in range(len(chr)):
        if chr[i]=="c" and chr[i]=="C":
            chr.remove(i)
    return(chr)
