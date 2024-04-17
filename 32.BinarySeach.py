# Given a sorted array of N integers and you need to find if Key (K) exists in the array or not, write an efficient code to do this.

# Note: Try to do it by implementing Binary Search both iteratively and recursively

# Sample Input
# N = 4, arr[] = { 1, 3, 4, 7 }, K = 3
# Sample Output
# true
# Sample Explanation
# Using Binary Search we find that key 3 exists in the array.
# Expected Time Complexity
# O(logN), where N is the length of the array

# Expected Space Complexity
# O(1), constant space solution

# Constraints
# 1<= N <= 10^6
# 1<= arr[i] <= 10^6

def binarySearch(arr,n,key):
    l=0
    r=n-1
    if key<arr[l]:
        return -1
    elif key>arr[r]:
        return -1
    while l<=r:
        m=l+(r-l)//2
        if arr[m]==key:
            return m
        elif arr[m]<key:
            l=m+1
        else:
            r=m-1
    return -1
arr=[1, 3, 4, 7]
k=3
ans=binarySearch(arr,len(arr),k)
print(ans)


# Bruteforce:-
def keyfind(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1