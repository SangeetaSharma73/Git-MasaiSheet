# Given an array A of N elements that contains elements from 1 to N-1. All elements occur once except one which occurs twice. Find the repeating element.

# Sample Input
# N = 5, A = [1, 3, 3, 2, 4].
# Sample Output
# Output: 3
# Sample Explanation
# Element 3 appears twice in the array. Hence it is the only repeating element.

# Expected Time Complexity
# O(N), where N is the size of the array

# Expected Space Complexity
# O(1), i.e., constant space complexity.

# Constraints
# 1 <= N <= 100000

#Approach-1
#Tc=O(n)
#Sc=O(n)
A = [1, 3, 3, 2, 4]
totalsum=sum(A)
originalSum=sum(set(A))
print(totalsum-originalSum)

#Approach2-
#Tc=O(n)
#Sc=O(1)
A=[1,3,3,2,4]
s1=0
for i in range(len(A)):
    s1+=A[i]
n=len(A)-1
s2=n*(n+1)//2
ans=s1-s2
print(ans)