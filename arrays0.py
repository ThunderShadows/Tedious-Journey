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