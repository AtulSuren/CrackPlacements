def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Variables to track which rows and columns need to be set to zero
    zero_rows = set()
    zero_cols = set()

    # Find the rows and columns that contain zeros
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set the rows to zero
    for row in zero_rows:
        for j in range(cols):
            matrix[row][j] = 0

    # Set the columns to zero
    for col in zero_cols:
        for i in range(rows):
            matrix[i][col] = 0

# Example usage
input_matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(input_matrix)
print(input_matrix)