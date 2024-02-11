# Given a positive integer N. Find the Nth fibonacci number.

# NOTE : In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. The beginning of the sequence is thus [0,1,2,3,5,8,13,21,34,...]

# Sample Input
# input: N = 5
# Sample Output
# A: 3
# Sample Explanation
# Fibonacci series: 0 1 1 2 3 5 8 13 .... Hence 5th fibonacci is: 3

# Expected Time Complexity
# O(N)

# Expected Space Complexity
# O(N), Auxillary space complexity.

# Constraints
# 1 <= N <= 100000

# Brute Force (Recursive) Solution:
def fibonacci_bruteforce(n):
    if n <= 1:
        return n
    else:
        return fibonacci_bruteforce(n-1) + fibonacci_bruteforce(n-2)
# Time Complexity: O(2^n) - Exponential time complexity due to redundant calculations.
# Space Complexity: O(n) - The recursive calls consume space on the call stack. In the worst case, the depth of the recursion tree is n, leading to O(n) space complexity.

#Better (Iterative) Solution:
def fibonacci_better(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b
    return b
# Time Complexity: O(n) - Linear time complexity. This solution iteratively calculates the Fibonacci numbers from the bottom-up.
# Space Complexity: O(1) - This solution uses only a constant amount of extra space regardless of the input value of n. It only stores two variables a and b.


# Optimal (Using Memoization) Solution:
def fibonacci_optimal(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_optimal(n-1, memo) + fibonacci_optimal(n-2, memo)
    return memo[n]
# Time Complexity: O(n) - Linear time complexity. This solution uses memoization to store intermediate results, avoiding redundant calculations.
# Space Complexity: O(n) - This solution uses memoization to store intermediate results in the memoization dictionary. The memoization dictionary can hold up to n entries, so the space complexity is O(n) in the worst case.