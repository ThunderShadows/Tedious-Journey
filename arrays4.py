# Next Permutation 
# Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

# Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.

# Examples:

# Input: arr = [2, 4, 1, 7, 5, 0]
# Output: [2, 4, 5, 0, 1, 7]

# Input: arr = [3, 2, 1]
# Output: [1, 2, 3]

# Input: arr = [3, 4, 2, 5, 1]
# Output: [3, 4, 5, 1, 2]

# Time Complexity: O(n) and Space Complexity: O(1)
class Solution:
    def next_permutation(self, arr):
        n = len(arr)
        pivot = -1
        
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break
        
        if pivot == -1:
            arr.reverse()
            return arr

        for i in range(n - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break

        left, right = pivot + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr

solution = Solution()
arr = [2, 4, 1, 7, 5, 0]
solution.next_permutation(arr)
print(" ".join(map(str, arr)))