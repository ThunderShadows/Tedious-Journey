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