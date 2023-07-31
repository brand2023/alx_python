def square_matrix_simple(matrix=[]):
    matrix1=[]
    matrix2=[]
    for row in matrix1:
        for i,k in enumerate(row):
            print("{:d}".format(k), end=" " if i<len(row)-1 else "")
        print()
    for row in matrix2:
        for i,k in enumerate(row):
            print("{:d}".format(k*k),  end=" " if i<len(row)-1 else "")
        print()
    matrix=list(map(matrix1, matrix2))
    return(matrix)