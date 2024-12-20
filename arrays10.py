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

# # Python program to find Maximum Product Subarray 
# # using nested loops

# # Function to returns the product of max product subarray
# def maxProduct(arr):
#     n = len(arr)
  
#     # Initializing result
#     result = arr[0]

#     for i in range(n):
#         mul = 1
      
#         # traversing in current subarray
#         for j in range(i, n):
#             mul *= arr[j]
          
#             # updating result every time
#             # to keep track of the maximum product
#             result = max(result, mul)
    
#     return result

# if __name__ == "__main__":
#     arr = [-2, 6, -3, -10, 0, 2]
#     print(maxProduct(arr))