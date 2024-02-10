# Given an array A having N positive integers. Sort the array A using bubble sort.

# Sample Input
# input: N = 5
# A : 5 1 6 3 7
# Sample Output
# A: 1 3 5 6 7
# Sample Explanation
# Self explanatory.

# Expected Time Complexity
# O(N*N)
# Expected Space Complexity
# O(1), i.e., constant space complexity.
# Constraints
# 1 <= N <= 1000

def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[5,1,6,3,7]
bubble(arr)
print(arr)
def selection(arr):
    for i in range(len(arr)):
        mini=i
        for j in range(i+1,len(arr)):
            if arr[mini]>arr[j]:
                mini=j
        arr[mini],arr[i]=arr[i],arr[mini]
a=[5 ,1 ,6 ,3, 7]
selection(a)
print(a)
    