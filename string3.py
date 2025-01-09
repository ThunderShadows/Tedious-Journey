# Python program to find the index of the first non repeating
# character by storing indices

# As the input string can only have lowercase 
# characters, the maximum characters will be 26
MAX_CHAR = 26

def nonRepeatingChar(s):
    vis = [-1] * MAX_CHAR

    # Iterate through the string
    for i in range(len(s)):

        # If the character is seen for the first time,
        # store its index
        if vis[ord(s[i]) - ord('a')] == -1:
            vis[ord(s[i]) - ord('a')] = i

        # If the character is seen again, mark it as -2
        else:
            vis[ord(s[i]) - ord('a')] = -2

    idx = float('inf')

    # Find the smallest index among all non-repeating 
    # characters
    for i in range(MAX_CHAR):
        if vis[i] >= 0:
            idx = min(idx, vis[i])

    # If non-repeating character is found, return it 
    # Else return '$'
    return '$' if idx == float('inf') else s[idx]

if __name__ == "__main__":
    s = "racecar"
    print(nonRepeatingChar(s))