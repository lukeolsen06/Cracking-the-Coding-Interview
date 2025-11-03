

# Question 1.8: Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

# BF: This runtime is O (M * N + k * (M + N)) where k is the number of zeros in the matrix. 
def zero_matrix(matrix):
    n = len(matrix[0])
    m = len(matrix)
    zero_positions = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_positions.append((i,j))
    
    for i, j in zero_positions:

        for col in range(n):
            matrix[i][col] = 0
        for row in range(m):
            matrix[row][j] = 0

    return matrix


# Optimized solution that uses two sets to store the rows and columns to zero, avoiding redundant zeroing when multiple zeros are in the same row or column. 
# This reduces the runtime to O (M * N). Space complexity is O (M + N) to store the sets.
def zero_matrix_optimized(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows_to_zero, cols_to_zero = set(), set()

    for i in range(m):
        for j in range(n):
            if j in cols_to_zero:
                continue
            if (matrix[i][j] == 0):
                rows_to_zero.add(i)
                cols_to_zero.add(j)
    
    for row in rows_to_zero:
        for j in range(n):
            matrix[row][j] = 0
    for col in cols_to_zero: 
        for i in range(m):
            matrix[i][col] = 0 

    return matrix    

matrix = [
            [6,3,4,1],
            [3,2,0,8],
            [4,0,2,7],
            [2,9,2,4],
        ]
        #[6,0,0,1]
        #[0,0,0,0]
        #[0,0,0,0]
        #[2,0,0,4]

matrix2 = [
            [3,4,2,1],
            [3,2,0,8],
            [4,1,2,7],
            [2,9,2,4],
        ]

        #[3,4,0,1]
        #[0,0,0,0]
        #[4,1,0,7]
        #[2,9,0,4]

print(zero_matrix_optimized(matrix))