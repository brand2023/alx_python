def square_matrix_simple(matrix=[]):
    for column in matrix:
        for i,k in enumerate(column):
            print("{:d}".format(k*k),  end=" " if i<len(row)-1 else "")
        print()
        