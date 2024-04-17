# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

# Notice that you may not slant the container.

# Sample Input
# array =  [1,8,6,2,5,4,8,3,7]
# Sample Output
# 49
# Sample Explanation
# Refer this image for understanding. The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Expected Time Complexity
# O(N), where N is the size of the array.

# Expected Space Complexity
# O(1),Auxilliary Space

# Constraints
#  n == height.length
#  2 <= n <= 3 * 10^4
#  0 <= height[i] <= 3 * 10^4

# * 