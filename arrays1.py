#Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.

# Examples:

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]

# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]

# Input: arr[] = [0, 0]
# Output: [0, 0]

# Time Complexity: O(n) and Space Complexity: O(1)
class Solution:
    def pushZerosToEnd(arr):
        count = 0
        n = len(arr)
        for i in range(n):        
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i]
                count += 1

    if __name__ == "__main__":
        arr = [1, 2, 0, 4, 3, 0, 5, 0]
        pushZerosToEnd(arr)
        for num in arr:
            print(num, end=" ")