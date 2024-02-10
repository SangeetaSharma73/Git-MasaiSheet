def reverse(A):
    prev=None
    curr=A
    while curr:
        Next=curr.next
        curr.next=prev
        prev=curr
        curr=Next
    return prev
        