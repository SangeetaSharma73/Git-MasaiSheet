# Given a square matrix of size N*N. Print the matrix after rotating it by 90 degrees in anti-clockwise direction.

# Sample Input
# input: N = 3
# Matrix : 1 2 3
# 	 4 5 6
# 	 7 8 9
# Sample Output
# Output: 3 6 9
# 	2 5 8
# 	1 4 7
# Sample Explanation
# Self explanatory.

# Expected Time Complexity
# O(N*N)

# Expected Space Complexity
# O(1), i.e., constant space complexity.

# Constraints
# 1 <= N <= 1000

arr=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(arr)):
    arr[i]=arr[i][::-1]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        arr[i],arr[j]=arr[j],arr[i]