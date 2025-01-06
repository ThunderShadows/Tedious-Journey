# Given two strings s1 and s2 consisting of lowercase characters, the task is to check whether the two given strings are anagrams of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different.

# Examples:

# Input: s1 = “geeks”  s2 = “kseeg”
# Output: true

# Input: s1 = “allergy”  s2 = “allergic”
# Output: false

# Input: s1 = "g", s2 = "g"
# Output: true

# Time Complexity: O(N) and Space Complexity: O(1)
MAX_CHAR = 26
def areAnagrams(s1, s2):
    freq = [0] * MAX_CHAR
    
    for ch in s1:
        freq[ord(ch) - ord('a')] += 1

    for ch in s2:
        freq[ord(ch) - ord('a')] -= 1

    for count in freq:
        if count != 0:
            return False
            
    return True

if __name__ == "__main__":
    s1 = "geeks"
    s2 = "kseeg"
    print("true" if areAnagrams(s1, s2) else "false")