def square_matrix_simple(matrix):
    for row in matrix:
        for i,k in enumerate(row):
            print("{:d}".format(k*k),  end=" " if i<len(row)-1 else "")
        print()
    return(matrix)