class Solution:
    def rotate(self, matrix):
        if not matrix:
            return []
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                # store the top-right element of the current layer in a temporary variable 
                tmp = matrix[n - 1 - j][i]
                # replace the top-right element with the bottom-right element
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                #replace the bottom-right element with the bottom-left element
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                # replace the bottom-left element with the top-left element
                matrix[j][n - i - 1] = matrix[i][j]
                # replace the top-left element with the stored temporary variable
                matrix[i][j] = tmp
        return matrix
