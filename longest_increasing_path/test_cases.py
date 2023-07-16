from solution import Solution
solution_obj = Solution()


# Test cases
test_cases = [
    # Example cases
    ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 3),
    ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),

    # Additional cases
    # 1x1 matrix
    ([[1]], 1),

    # 2x2 matrix
    ([[1, 2], [3, 4]], 3),

    # 2x2 matrix with no increasing path
    ([[4, 3], [2, 1]], 3),

    # 3x3 matrix with multiple increasing paths
    ([[9, 8, 7], [5, 6, 1], [4, 3, 2]], 8),

    # 4x4 matrix with wrap-around not allowed
    ([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]], 16),

    # Empty matrix
    ([], 0)
]

# Perform the test cases
for i, (matrix, expected) in enumerate(test_cases):
    result = solution_obj.longestIncreasingPath(matrix)
    print(f"Test Case #{i+1}")
    print("Input Matrix:")
    for row in matrix:
        print(row)
    print("Expected Output:", expected)
    print("Result:", result)
    print()