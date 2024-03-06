import numpy as np

# function to take nxm matrix, and simulate two lane two way intersection with numerical values
# exmple: 6x6 matrix
# matrix originally looks like this:
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# matrix after function call looks like this:
# 0 0 1 2 0 0
# 0 0 1 2 0 0
# 3 3 5 5 3 3
# 4 4 5 5 4 4
# 0 0 1 2 0 0
# 0 0 1 2 0 0

# example 2: 7x7 matrix
# matrix originally looks like this:
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0

# matrix after function call looks like this:
# 0 0 1 2 0 0 0
# 0 0 1 2 0 0 0
# 3 3 5 5 3 3 0
# 4 4 5 5 4 4 0
# 0 0 1 2 0 0 0
# 0 0 1 2 0 0 0




# 1= southbound, 2= northbound, 3= eastbound, 4= westbound, 5= intersection area

import numpy as np

def create_intersection_matrix(n, m):
    # Initialize the matrix with zeros
    matrix = np.zeros((n, m))
    
    # Determine the central points
    center_n = n // 2 # center of rows/height
    center_m = m // 2 # center of columns/width
    
    # Adjust for even dimensions - to ensure the intersection is centered
    n_start = center_n - 1 if n % 2 == 0 else center_n
    m_start = center_m - 1 if m % 2 == 0 else center_m
    
    # Create intersection area
    for i in range(n_start, n_start+2):
        for j in range(m_start, m_start+2):
            matrix[i][j] = 5
    
    # Create lanes leading to the intersection
    # Southbound and Northbound lanes
    for i in range(n_start):
        matrix[i][m_start] = 1
        matrix[i][m_start+1] = 2
    for i in range(n_start+2, n):
        matrix[i][m_start] = 1
        matrix[i][m_start+1] = 2
    
    # Eastbound and Westbound lanes
    for j in range(m_start):
        matrix[n_start][j] = 4
        matrix[n_start+1][j] = 3
    for j in range(m_start+2, m):
        matrix[n_start][j] = 4
        matrix[n_start+1][j] = 3
    
    return matrix

# Example usage
n, m = 6, 6 # For a 6x6 matrix
print(create_intersection_matrix(n, m))

print("\n")
print("\n")

n, m = 7, 7 # For a 7x7 matrix
print(create_intersection_matrix(n, m))

