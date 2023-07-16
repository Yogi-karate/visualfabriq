from solution import Solution
solution_obj = Solution()

# Empty array test cases
prices = []
print(solution_obj.maxProfit(prices))  # Output: 0

# array with strictly ascending order
prices = [1, 2, 3, 4, 5]
# Output: 4 (Buy on day 1, sell on day 5)
print(solution_obj.maxProfit(prices))

# array with strictly descending order
prices = [5, 4, 3, 2, 1]
print(solution_obj.maxProfit(prices))  # Output: 0 (No profit can be made)

# Test case with prices where the maximum profit occurs at the beginning:
prices = [10, 7, 5, 8, 11, 9]
# Output: 6 (Buy on day 2, sell on day 5)
print(solution_obj.maxProfit(prices))

# Test case with prices where the maximum profit occurs at the end:
prices = [3, 8, 6, 5, 10]
# Output: 7 (Buy on day 1, sell on day 5)
print(solution_obj.maxProfit(prices))

# Test case with prices containing multiple peaks and valleys:
prices = [2, 1, 4, 6, 3, 9, 2, 5]
# Output: 8 (Buy on day 2, sell on day 5, buy on day 6, sell on day 7)
print(solution_obj.maxProfit(prices))

# Test case with prices where no profit can be made:
prices = [4, 3, 2, 1]
print(solution_obj.maxProfit(prices))  # Output: 0 (No profit can be made)
