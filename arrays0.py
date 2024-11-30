
# SECOND LARGEST ELEMENT IN AN ARRAY
# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.
# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.

# Optimized solution having time complexity O(n) and space complexity O(1) 
class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        largest = -1
        secondlargest = -1

        for i in range(n):
            if arr[i] > largest:
                secondlargest = largest
                largest = arr[i]
            elif arr[i] > secondlargest and arr[i] != largest:
                secondlargest = arr[i]
        
        return secondlargest

if __name__ == "__main__":
    arr = [10,5,10]
    sol = Solution()
    print(sol.getSecondLargest(arr))