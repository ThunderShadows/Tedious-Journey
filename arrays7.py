# Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.
# Examples:

# Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
# Output: 8

# Input: prices[] = [7, 6, 4, 3, 1]
# Output: 0 

# Input: prices[] = [1, 3, 6, 9, 11]
# Output: 10 

# Time Complexity: O(n) and Space Complexity: O(1)
def maxProfit(prices):
    minSoFar = prices[0]
    res = 0
    for i in range(1, len(prices)):
        minSoFar = min(minSoFar, prices[i])             
        res = max(res, prices[i] - minSoFar)
    
    return res

if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(maxProfit(prices))