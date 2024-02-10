# Given an integer N. Print the numbers from 1 to N and for multiples of ‘3’ print “Fizz” instead of the number, for the multiples of ‘5’ print “Buzz” and for multiples of both 5 and 3 print "FizzBuzz"

# Sample Input
# input: N = 10
# Sample Output
# Output: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz
# Sample Explanation
# Self explanatory.

# Expected Time Complexity
# O(N)

# Expected Space Complexity
# O(1), i.e., constant space complexity.

# Constraints
# 1 <= N <= 100000
N=10
for i in range(1,N+1):
    if i%3==0 and i%5==0:
        print('FizzBuzz',end=' ')
    elif i%3==0:
        print('Fizz',end=' ')
    elif i%5==0:
        print('Buzz',end=' ')
    else:
        print(i,end=' ')

    