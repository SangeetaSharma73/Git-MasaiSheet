# Check for palindrome
# Given a string of length N. Check if the given string is a palindrome without using any built-in functionality.

# Sample Input
# input: N = 9, string: malayalam
# Sample Output
# Output: Yes
# Sample Input
# input: N = 5, string: masai
# Sample Output
# Output: No
# Sample Explanation
# Self explanatory.

# Expected Time Complexity
# O(N), where N is the size of the string

# Expected Space Complexity
# O(1), i.e., constant space complexity.

# Constraints
# 1 <= N <= 100000

#slicing 
#Tc= O(n)
#Sc=O(1)
def palindrome(s):
    if s==s[::-1]:
        return True
    return False