def matrix_multiply(A, B):
    """
    Multiplies two matrices A and B.
    
    Args:
    A: List of lists, where each sublist represents a row in the matrix.
    B: List of lists, where each sublist represents a row in the matrix.
    
    Returns:
    result: The resulting matrix after multiplication.
    """
    # Number of rows in A and B
    rows_A = len(A)
    rows_B = len(B)
    
    # Number of columns in A and B
    cols_A = len(A[0])
    cols_B = len(B[0])
    
    # Ensure matrices A and B can be multiplied
    if cols_A != rows_B:
        raise ValueError("Number of columns in A must be equal to number of rows in B.")
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Example usage:
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

result = matrix_multiply(A, B)
for row in result:
    print(row)
