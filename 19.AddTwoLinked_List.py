# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Sample Input
# list1 = [2->4->3], list2 = [5->6->4]
# Sample Output
# list = [7->0->8]
# Sample Explanation
# The number represented by the first linked list is 342, while the number represented by the second linked list is 465. Adding them, the new list represents their sum 807. 
# Expected Time Complexity
# O(m + n), where m and n are number of nodes in first and second lists respectively. The lists needs to be traversed only once.

# Expected Space Complexity
# O(k), where k is the number of digits.

# Constraints
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
def Node():
    pass

def f(A,B):
    l1=A
    l2=B
    carry=0
    dummy=Node(-1)
    curr=dummy
    while l1 or l2 or carry:
        s=0
        if l1:
            s+=l1.data
            l1=l1.next
        if l2:
            s+=l2.data
            l2=l2.next
        s+=carry
        carry=s//10
        curr.next=Node(s%10)
        curr=curr.next
    return dummy.next
