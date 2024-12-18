# Given an unsorted array arr[] with both positive and negative elements, the task is to find the smallest positive number missing from the array.
# Examples:

# Input: arr[] = {2, -3, 4, 1, 1, 7}
# Output: 3

# Input: arr[] = {5, 3, 2, 5, 1}
# Output: 4

# Input: arr[] = {-8, 0, -1, -4, -3}
# Output: 1

# Time Complexity - O(n) Time and O(1) Space

def missingNumber(arr):
    n = len(arr)
    for i in range(n):

        # if arr[i] is within the range 1 to n
        # and arr[i] is not placed at (arr[i]-1)th index in arr
        while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:

            # then swap arr[i] and arr[arr[i]-1] to place arr[i]
            # to its corresponding index
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp

    # If any number is not at its corresponding index, then it
    # is the missing number
    for i in range(1, n + 1):
        if i != arr[i - 1]:
            return i

    # If all number from 1 to n are present 
    # then n + 1 is smallest missing number
    return n + 1


if __name__ == '__main__':
    arr = [2, -3, 4, 1, 1, 7]
    print(missingNumber(arr))

# C++ program to find the first positive missing number 
# using Sorting

# # Function to find the first positive missing number
# def missingNumber(arr):
#     arr.sort()

#     # res will hold the current smallest missing number,
#     # initially set to 1
#     res = 1
#     for num in arr:

#         # If we have found 'res' in the array,
#         # 'res' is no longer missing, so increment it
#         if num == res:
#             res += 1

#         # If the current element is larger than 'res',
#         # 'res' cannot be found in the array,
#         # so it is our final answer
#         elif num > res:
#             break
#     return res


# if __name__ == "__main__":

#     arr = [2, -3, 4, 1, 1, 7]
#     print(missingNumber(arr))