# Given an array of integers arr, reverse it in-place.
# Examples:

# Input: arr = [1, 4, 3, 2, 6, 5]
# Output: [5, 6, 2, 3, 4, 1]

# Input: arr = [4, 5, 2]
# Output: [2, 5, 4]

# Input: arr = [1]
# Output: [1]

# Time Complexity: O(n) and Space Complexity: O(1)
class Solution:
    def reverseArray(arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1

    if __name__ == "__main__":
        arr = [1, 4, 3, 2, 6, 5]

        reverseArray(arr)
    
        for i in range(len(arr)):
            print(arr[i], end=" ")