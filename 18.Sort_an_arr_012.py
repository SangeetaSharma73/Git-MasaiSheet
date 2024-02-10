# Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.

# Sample Input
# array = {0, 1, 2, 0, 1, 2}
# Sample Output
# array = {0, 0, 1, 1, 2, 2}
# Sample Explanation
# The array on sorting gives the resultant array as shown in the output  
# Expected Time Complexity
# O(N), where N is the size of the array.
# Expected Space Complexity
# O(1),Auxilliary Space
# Constraints
#  n == nums.length
#  1 <= n <= 300
#  array[i] is 0, 1, or 2.

#Ap-1Tc=O(nlogn)
arr=[0, 1, 2, 0, 1, 2]
arr.sort()
print(arr)

#Ap2-Tc=O(n)
arr=[0, 1, 2, 0, 1, 2]
zero_count=0
one_count=0
two_count=0
for i in range(len(arr)):
    if arr[i]==0:
        zero_count+=1
    elif arr[i]==1:
        one_count+=1
    else:
        two_count+=1
for i in range(zero_count):
    arr[i]=0
for j in range(zero_count,one_count+zero_count):
    arr[j]=1
for k in range(zero_count+one_count,two_count+one_count+two_count):
    arr[k]=2
print(arr)
