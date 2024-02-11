# Two Numbers in sorted array whose sum is K
# Given a sorted array of integers nums and an integer K, return indices of the two numbers such that they add up to K.

# Note: You can assume that the answer always exists

# Sample Input
# array = [2,7,11,15], K = 9
# Sample Output
# [0,1]
# Sample Explanation
# As seen from the sample input, the values at index 0 and 1 add up to the required value of 9. Therefore, the output is [0,1].

# Expected Time Complexity
# O(N),where N is the size of the array.

# Expected Space Complexity
# O(1), Auxillary space complexity.

# Constraints
#  2 <= nums.length <= 103
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9


#Tc=O(n)
#Sc=O(1)
array = [2,7,11,15]
K = 9
i=0
j=len(array)-1
ans='No'
while i<j:
    if array[i]+array[j]==K:
        ans='Yes'
        break
    elif array[i]+array[j]<K:
        i+=1
    else:
        j-=1
print(ans)
        
#Tc=O(n^2)
#Sc=O(1)
ans='No'
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]+array[j]==K:
            ans='Yes'
            break
print(ans)
            
            
            
        
