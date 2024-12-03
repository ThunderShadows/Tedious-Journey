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
