def naive_matrix_multiply(A, B):
    n = len(A) # SC: O(1)
    C = [[0] * n for _ in range(n)] # SC: O[n**2]
    for i in range(n): # TC: O[n]
        for j in range(n): # TC: O[n]
            for k in range(n): # TC: O[n]
                C[i][j] += A[i][k] * B[k][j] # O[1]
    return C #TC: O[1]

'''
TC: O[n**3]
SC: O[n**2]
'''

# Optimise Approch

def strassen_matrix_multiply(A, B):
    # Base case when the matrix is 1x1
    if len(A) == 1: #TC: O[1]
        return [[A[0][0] * B[0][0]]] #TC: O[1]

    # Split matrices into quadrants
    n = len(A) #TC: O[1] SC: O[1]
    mid = n // 2 #TC: O[1] SC: O[1]
    A11 = [row[:mid] for row in A[:mid]] #TC: O[1] SC: O[n]
    A12 = [row[mid:] for row in A[:mid]] #TC: O[1] SC: O[n]
    A21 = [row[:mid] for row in A[mid:]] #TC: O[1] SC: O[n]
    A22 = [row[mid:] for row in A[mid:]] #TC: O[1] SC: O[n]
    B11 = [row[:mid] for row in B[:mid]] #TC: O[1] SC: O[n]
    B12 = [row[mid:] for row in B[:mid]] #TC: O[1] SC: O[n]
    B21 = [row[:mid] for row in B[mid:]] #TC: O[1] SC: O[n]
    B22 = [row[mid:] for row in B[mid:]] #TC: O[1] SC: O[n]

    # Compute the 7 products
    P1 = strassen_matrix_multiply(add_matrices(A11, A22), add_matrices(B11, B22)) #TC: O[1] SC: O[1]
    P2 = strassen_matrix_multiply(add_matrices(A21, A22), B11) #TC: O[1] SC: O[1]
    P3 = strassen_matrix_multiply(A11, subtract_matrices(B12, B22)) #TC: O[1] SC: O[1]
    P4 = strassen_matrix_multiply(A22, subtract_matrices(B21, B11)) #TC: O[1] SC: O[1]
    P5 = strassen_matrix_multiply(add_matrices(A11, A12), B22) #TC: O[1] SC: O[1]
    P6 = strassen_matrix_multiply(subtract_matrices(A21, A11), add_matrices(B11, B12)) #TC: O[1] SC: O[1]
    P7 = strassen_matrix_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22)) #TC: O[1] SC: O[1]

    # Combine the 7 products to get the result
    C11 = add_matrices(subtract_matrices(add_matrices(P1, P4), P5), P7) #TC: O[1] SC: O[1]
    C12 = add_matrices(P3, P5) #TC: O[1] SC: O[1]
    C21 = add_matrices(P2, P4) #TC: O[1] SC: O[1]
    C22 = add_matrices(subtract_matrices(add_matrices(P1, P3), P2), P6) #TC: O[1] SC: O[1]

    # Combine quadrants into a single matrix
    C = [] #TC: O[1] SC: O[1]
    for i in range(mid): #TC: O[n]
        C.append(C11[i] + C12[i]) #TC: O[1] 
    for i in range(mid): #TC: O[n]
        C.append(C21[i] + C22[i]) #TC: O[1] 

    return C

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]
