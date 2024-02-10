# Write a program to print Binary representation of a given number.

# Sample Input
# N = 7
# Sample Output
# 00000000000000000000000000000111
# Sample Explanation
# Self Explanatory
# Expected Time Complexity
# O(1), constant time complexity

# Expected Space Complexity
# O(1), constant space complexity

# Constraints
# 0<= N <= (2^32)-1

# Brute Force Solution:
# Time Complexity: O(log n) - The number of iterations is proportional to the number of bits in the binary representation of the decimal number.
# Space Complexity: O(log n) - Space required to store the binary representation.
def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary if binary else "0"
ans=decimal_to_binary(10)
print(ans)
#Using Arr
def decimal_to_binary(n):
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    return "".join(binary[::-1]) if binary else "0"

#Optimal Solution:
# Time Complexity: O(1) - The bin() function directly converts the decimal number to its binary representation.
# Space Complexity: O(log n) - Space required to store the binary representation.
def decimal_to_binary(n):
    return bin(n)[2:]
n=7
ans=decimal_to_binary(n)
print(ans)

