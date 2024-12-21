# Given a string s, the task is to convert it into integer format without utilizing any built-in functions. If the string cannot be converted into integer, then return 0.
# Examples:

# Input: s = "-123"
# Output: -123

# Input: s = " -"
# Output: 0

# Input: s = " 1231231231311133"
# Output: 2147483647

# Python Program to implement atoi() function

def myAtoi(s: str) -> int:
    sign = 1
    res = 0
    idx = 0

    # Ignore leading whitespaces
    while idx < len(s) and s[idx] == ' ':
        idx += 1

    # Store the sign of number
    if idx < len(s) and (s[idx] == '-' or s[idx] == '+'):
        if s[idx] == '-':
            sign = -1
        idx += 1

    # Construct the number digit by digit
    while idx < len(s) and '0' <= s[idx] <= '9':

        # Append current digit to the result
        res = 10 * res + (ord(s[idx]) - ord('0'))

        # Handling overflow/underflow test case
        if res > (2**31 - 1):
            return sign * (2**31 - 1) if sign == 1 else -2**31

        idx += 1

    return res * sign

s = "  -0012g4"
print(myAtoi(s))