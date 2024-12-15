# Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].


# Input: arr[] = [-2, 6, -3, -10, 0, 2]
# Output: 180

# Input: arr[] = [-1, -3, -10, 0, 6]
# Output: 30

# Input: arr[] = [2, 3, 4] 
# Output: 24 

# Time Complexity: O(n) and Space Complexity: O(1)
def maxProduct(arr):
    n = len(arr)
    maxProd = float('-inf')
  
    # leftToRight to store product from left to Right
    leftToRight = 1
  
    # rightToLeft to store product from right to left
    rightToLeft = 1
  
    for i in range(n):
        if leftToRight == 0:
            leftToRight = 1
        if rightToLeft == 0:
            rightToLeft = 1
      
        # calculate product from index left to right
        leftToRight *= arr[i]
      
        # calculate product from index right to left
        j = n - i - 1
        rightToLeft *= arr[j]
        maxProd = max(leftToRight, rightToLeft, maxProd)
    
    return maxProd

arr = [-2, 6, -3, -10, 0, 2]
print(maxProduct(arr))