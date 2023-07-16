from solution import Solution
solution_obj = Solution()

test_cases = [
    # 2x2 matrix
    [[1, 2], [3, 4]],  # Expected: [[3, 1], [4, 2]]

    # 3x3 matrix
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # 4x4 matrix
    [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],  # Expected: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    # 1x1 matrix (single element)
    [[99]],  # Expected: [[99]]

    # Empty matrix
    [],  # Expected: []

    # Square matrix with all elements the same
    [[2, 2, 2], [2, 2, 2], [2, 2, 2]],  # Expected: [[2, 2, 2], [2, 2, 2], [2, 2, 2]]

    # Square matrix with distinct elements
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
]

# Perform the rotation and print the results
for i, matrix in enumerate(test_cases):
    result = solution_obj.rotate(matrix)
    print(f"Test Case #{i+1}")
    print("Input Matrix:")
    for row in matrix:
        print(row)
    print("Rotated Matrix:")
    for row in result:
        print(row)
    print()