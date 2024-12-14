# Given an array arr[], the task is to find the subarray that has the maximum sum and return its sum.

# Examples:

# Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
# Output: 11

# Input: arr[] = {-2, -4}
# Output: -2

# Input: arr[] = {5, 4, 1, 7, 8}
# Output: 25

# Time Complexity: O(n) and Space Complexity: O(1)

def maxSubarraySum(arr):
    
    res = arr[0]
    maxEnding = arr[0]

    for i in range(1, len(arr)):
        maxEnding = max(maxEnding + arr[i], arr[i])
        res = max(res, maxEnding)
    
    return res

arr = [2, 3, -8, 7, -1, 2, 3]
print(maxSubarraySum(arr))

# # Python Program to find the maximum subarray sum using nested loops

# # Function to find the sum of subarray with maximum sum
# def maxSubarraySum(arr):
#     res = arr[0]
  
#     # Outer loop for starting point of subarray
#     for i in range(len(arr)):
#         currSum = 0
      
#         # Inner loop for ending point of subarray
#         for j in range(i, len(arr)):
#             currSum = currSum + arr[j]
          
#             # Update res if currSum is greater than res
#             res = max(res, currSum)
          
#     return res

# if __name__ == "__main__":
#     arr = [2, 3, -8, 7, -1, 2, 3]
#     print(maxSubarraySum(arr))