import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [3, 6, 9, 2],
    [4, 8, 2, 6]
])

# Expected output:
# 1 2 3 4
# 2 4 6 8
# 3 6 9 2
# 4 8 2 6

for i in range(4):
    row = ""
    for j in range(4):
        if True:
            row += str(matrix[i, j]) + " "
        else:
            row += "  "
    print(row)

print("")

# NOTE: Your solution should use the elements from the matrix, no hard-coding values!

# TODO 1.1: Create a nested for-loop that produces the following output:
# 1 2 3 4
#   4 6 8
#     9 2
#       6



# END TODO 1.1
print("")

# TODO 1.2: Create a nested for-loop that produces the following output:
# 1      
# 2 4    
# 3 6 9  
# 4 8 2 6



# END TODO 1.2
print("")

# TODO 1.3: Create a nested for-loop that produces the following output:
#       4
#     6 8
#   6 9 2
# 4 8 2 6



# END TODO 1.3
print("")

# TODO 1.4: Create a nested for-loop that produces the following output:
# 1 2 3 4
# 2 4 6  
# 3 6    
# 4      



# END TODO 1.4