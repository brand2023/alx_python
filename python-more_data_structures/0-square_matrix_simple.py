def square_matrix_simple(matrix):
    for row in matrix:
        for i,k in enumerate(row):
            print("{:d}".format(k*k),  end=" " if i<len(row)-1 else "")
        print()
        for i in range(3):
            matrix.append([row[i] for row in matrix])
    return(matrix)