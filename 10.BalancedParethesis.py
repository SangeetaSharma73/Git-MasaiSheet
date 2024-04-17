# Given a string S having N characters. Any of the characters of the string are either of '(', '{', '[', ')', '}', ']'. Check whether the pairs and the orders of '{', '}', '(', ')', '[', ']' are correct or not.

# Sample Input
# input: N = 6
# S : [()]{}
# Sample Output
# A: -"Yes"
# Sample Input
# input: N = 4
# S : [(])
# Sample Output
# A: -"No"
# Sample Explanation
# Self explanatory.

# Expected Time Complexity
# O(N), where N is the size of the string S.

# Expected Space Complexity
# O(N), where N is the size of the string S.

# Constraints
# 1 <= N <= 100000

#1.Using Stack
#TC=O(n)
#Sc=O(n)
def f(s):
    st=[]
    for i in range(len(s)):
        if s[i]=='(' or s[i]=='{' or s[i]=='[':
            st.append(s[i])
        elif st and ((st[-1]=='(' and s[i]==')') or (st[-1]=='{' and s[i]=='}') or (st[-1]=='[' and s[i]==']')):
            st.pop()
        else:
            return 'not balanced'
    if not st:
        return 'balanced'
    else:
        return 'not balanced'

            
for i in range(1):
    s='[()]{}'
    ans=f(s)
    print(ans)