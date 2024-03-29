# Print all subsequences of a string
# Given a string, we have to find out all subsequences of it.

# Note: A String is a subsequence of a given String, that is generated by deleting some character of a given string without changing its order.

# Sample Input
# abc
# Sample Output
# a, b, c, ab, bc, ac, abc
# Sample Explanation
# Generate all subsequence of string "abc"
# Expected Time Complexity
# O(2^N*l), where N is length of string to find subsequences and l is length of binary string.

# Expected Space Complexity
# O(N), Auxiliary space

# Constraints
# 1 <= N <= 10


#backtracking-
# Time Complexity:
# The time complexity of generating all subsequences using the provided code is exponential, O(2^N), where N is the length of the string arr. This is because each character in the string has two options: to be included in the subsequence or not.
# Space Complexity:
# The space complexity of the provided code is also exponential, O(2^N). This is because the recursive calls create a call stack, and at each level of recursion, there are potentially two recursive calls.

#Possible subsequence- 2^N-1(without empty one)
def subsequence(arr,l,n,ans):
    if l<=n and ans!='':
        print(ans)
        
    for i in range(l,n):
        subsequence(arr,i+1,n,ans+arr[i])
arr='abc'
subsequence(arr,0,3,'')