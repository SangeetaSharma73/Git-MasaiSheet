# Given an one dimensional array of size N having both positive and negative integers. Find the sum of subarray such that it has the largest sum among all subarrays.

# Sample Input
# array = [2, -3, 4, -1, -2, 1, 5, -3]
# Sample Output
# Output: 7
# Sample Explanation
# The subarray → [4, -1, -2, 1, 5] gives sum 7 which is the largest sum among all subarrays. Hence the answer is 7.

# Expected Time Complexity
# O(N), where N is the size of the array

# Expected Space Complexity
# O(1), i.e., constant space complexity.

# Constraints
# 1 <= N <= 100000
# -100000 <= Array element <= 100000


#Tc=O(n)
arr=[4, -1, -2, 1, 5]
s=0
maximum=-float('inf')
for i in arr:
    s+=i
    if s>maximum:
        maximum=s
    if s<0:
        s=0
print(maximum)

#BruteForce- O(n^2)
for i in range(len(arr)):
    s=0
    for j in range(i+1):
        s+=arr[j]
    if maximum<s:
        maximum=s
print(maximum)