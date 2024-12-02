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