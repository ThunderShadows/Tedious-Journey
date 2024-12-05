# Majority Element in an Array of size n such that it appears more than n/3 times
# You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

# Note: The answer should be returned in an increasing format.

# Examples:

# Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
# Output: [5, 6]

# Input: arr[] = [1, 2, 3, 4, 5]
# Output: []

# Time Complexity: O(n) and Space Complexity: O(n)
def findMajority(arr):
    n = len(arr)
    freq = {}
    res = []

    for ele in arr:
        freq[ele] = freq.get(ele, 0) + 1

    for ele, cnt in freq.items():
        

        if cnt > n // 3:
            res.append(ele)

    if len(res) == 2 and res[0] > res[1]:
        res[0], res[1] = res[1], res[0]
    return res

if __name__ == "__main__":
    arr = [2, 2, 3, 1, 3, 2, 1, 1]
    res = findMajority(arr)
    for ele in res:
        print(ele, end=" ")