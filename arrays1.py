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