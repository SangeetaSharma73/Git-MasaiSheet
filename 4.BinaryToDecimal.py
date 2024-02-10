#BruteForce:-
# Time Complexity: O(n) - Where n is the number of digits in the binary number.
# Space Complexity: O(1) - Constant space used.
def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal
ans=binary_to_decimal('111')
print(ans)
