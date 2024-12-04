# Rotate an array by d elements in clockwise direction 
# Given an unsorted array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

# Note: Consider the array as circular.

# Examples :

# Input: arr[] = [1, 2, 3, 4, 5], d = 2
# Output: [3, 4, 5, 1, 2]

# Input: arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], d = 3
# Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]

# Input: arr[] = [7, 3, 9, 1], d = 9
# Output: [3, 9, 1, 7]

# Time Complexity: O(n) and Space Complexity: O(1)
class Solution:
    @staticmethod
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    @staticmethod
    def rotateArr(arr, d):
        n = len(arr)
        d %= n
        Solution.reverse(arr, 0, d - 1)
        Solution.reverse(arr, d, n - 1)
        Solution.reverse(arr, 0, n - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    Solution.rotateArr(arr, d)
    for i in range(len(arr)):
        print(arr[i], end=" ")
