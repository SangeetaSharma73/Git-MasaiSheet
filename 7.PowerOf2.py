# Given a positive integer N. Check if it is a power of two or not.

# Sample Input
# input: N = 4
# Sample Output
# Output: Yes
# Sample Explanation
# 4 can be represented as 2*2. Hence it's prime factorisation includes no prime except 2. Hence it can be represented as a power of 2.

# Expected Time Complexity
# O(log(N)), where N is the positive integer.

# Expected Space Complexity
# O(1), i.e., constant space complexity.

# Constraints
# 1 <= N <= 10000000000000
N=4
i=0
ans=False
while i**2<N:
    if i**2==N:
        ans=True
        break
print(ans)
    