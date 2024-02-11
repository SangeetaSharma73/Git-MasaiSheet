# Given two integer N and M. Calculate the gcd of N and M.

# Sample Input
# input: N = 10, M = 6
# Sample Output
# Output: 2
# Sample Explanation
# 2 is the biggest factor that divides both 10 and 6.

# Expected Time Complexity
# O(log(MAX(N,M)))

# Expected Space Complexity
# O(1), i.e., constant space complexity.

# Constraints
# # 1 <= N,M <= 1000000000

#Approach1-Linear
# Time Complexity: O(min(a, b)) - This is because we iterate from 1 up to the minimum of the two numbers.
def gcd_bruteforce(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd


# Approach2-Recursive 
#Tc=O(log min(a, b)) 
def GCD_better(a,b,c=1):
    if b%a==0:
        return a,c
    else:
        return GCD_better(b%a,a,c+1)

ans,c=GCD_better(12,8)
print(ans,c)

# Better Solution(Euclidean Algorithm):Iterative
#Time Complexity: O(log min(a, b)) - This is the time complexity of the Euclidean algorithm. It converges rapidly towards the GCD.
def gcd_better(a, b):
    while b:
        a, b = b, a % b
    return a