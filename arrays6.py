# Given an array of stock prices, find the maximum profit that can be made by buying and selling the stock once. The catch is that you can't sell the stock on the same day you buy it. 

# Input: prices[] = [100, 180, 260, 310, 40, 535, 695]
# Output: 865

# Input: prices[] = [4, 2, 2, 2, 4]
# Output: 2

# Time Complexity: O(n) and Space Complexity: O(1)
def maximumProfit(prices):
    n = len(prices)
    lMin = prices[0]  # Local Minima
    lMax = prices[0]  # Local Maxima
    res = 0
  
    i = 0
    while i < n - 1:
      
        # Find local minima
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1
        lMin = prices[i]
        
        # Local Maxima
        while i < n - 1 and prices[i] <= prices[i + 1]:
            i += 1
        lMax = prices[i]
      
        # Add current profit
        res += (lMax - lMin)
  
    return res


if __name__ == "__main__":
    prices = [100, 180, 260, 310, 40, 535, 695]
    print(maximumProfit(prices))