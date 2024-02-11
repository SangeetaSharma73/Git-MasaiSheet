# Print all Permutations of an Array
# Given an array of distinct integers of size N, the task is to generate and print all permutations of the given array.

# Sample Input
# N = 3
# arr[] = {0, 1, 2}
# Sample Output
# 0 1 2
# 1 0 2
# 0 2 1
# 2 0 1
# 1 2 0
# 2 1 0
# Sample Explanation
# Generating all permutations of the array by checking all possible numbers at all index.
# Expected Time Complexity
# O(N*N!), where N is the size of the array

# Expected Space Complexity
# O(N), Auxiliary space

# Constraints
# 1 <= N <= 6
# -10 <= arr[i] <= 10
# All the integers of array are unique


#Using Backtracking-
# The time complexity of generating all permutations using backtracking is O(N!), where N is the length of the array. This is because there are N! possible permutations of an array of length N.
# Space Complexity:
# The space complexity of the provided code is O(N), where N is the length of the array. This is because additional space is used for the recursive call stack, which can have at most N frames.
def Permutation(arr,l,n):
    if l==n:
        print(arr)
    for i in range(l,n):
        arr[l],arr[i]=arr[i],arr[l]
        Permutation(arr,l+1,n)
        arr[l],arr[i]=arr[i],arr[l]
arr=[1,2,3]
ans=Permutation(arr,0,3)
        