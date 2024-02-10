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
def Balancedparenthesis(s):
    st=[]
    if len(s)%2==1:
        return False
    for i in s:
        if i=='(' or i=='{' or i=='[':
            st.append(i)
        elif i==')':
            while st and ((st[-1]!='(' and i==')') or (st[-1]=='{' and i=='}') or (st[-1]=='[' and i==']')):
                st.pop()
        else:
            return False
    if not st:
        return True
    else:
        return False

                
    
s='[()]{}'
ans=Balancedparenthesis(s)
print(ans)