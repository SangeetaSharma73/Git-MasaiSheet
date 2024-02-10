# Given an integer N. Check whether N is prime or not.
# Sample Input
# input: N = 10
# Sample Output
# Output: No
# Sample Input
# input: N = 7
# Sample Output
# Output: Yes
# Sample Explanation
# Self explanatory.

# Expected Time Complexity
# O(sqrt{N})

# Expected Space Complexity
# O(1), i.e., constant space complexity.

# Constraints:
#     1 <= N <= 1000000000
import math
N=13
def CheckPrime(N):
    for i in range(2,int(N**0.5)+1):
        if N%i==0:
            return False
    return True
ans=CheckPrime(N)
print(ans)
        
        