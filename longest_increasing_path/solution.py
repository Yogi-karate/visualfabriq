class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]  # Memoization table to store path lengths

        def dfs(i, j):
            if memo[i][j] != 0:  # If the path length is already computed for this cell, return it
                return memo[i][j]

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible directions to move

            # Try moving in each direction
            for dx, dy in directions:
                x, y = i + dx, j + dy

                # Check if the new cell is within the boundary and has a greater value
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    memo[i][j] = max(memo[i][j], dfs(x, y))  # Update the path length with the longest increasing path from the new cell

            memo[i][j] += 1  # Increment the path length for the current cell
            return memo[i][j]

        # Iterate through each cell and perform DFS to find the longest increasing path
        max_path = 0
        for i in range(m):
            for j in range(n):
                max_path = max(max_path, dfs(i, j))

        return max_path
