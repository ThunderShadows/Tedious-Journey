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