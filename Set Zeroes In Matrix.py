def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    
    zerorows = set()
    zerocols = set()

    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zerorows.add(i)
                zerocols.add(j)

    
    for row in zerorows:
        for j in range(cols):
            matrix[row][j] = 0

    
    for col in zerocols:
        for i in range(rows):
            matrix[i][col] = 0

inputmatrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(inputmatrix)
print(inputmatrix)
