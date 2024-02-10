# Implement a Stack using two queues q1 and q2 such that the stack supports two operations push() and pop()

# Sample Input
# push(2)
# push(3)
# pop()
# push(4)
# pop()
# Sample Output
# 3 4
# Sample Explanation
# push(2) the stack will be {2}
# push(3) the stack will be {2 3}
# pop()   poped element will be 3 the stack will be {2}
# push(4) the stack will be {2 4}
# pop()   poped element will be 4  
# Expected Time Complexity
# O(1) for push() and O(N) for pop() (or vice-versa).

# Expected Space Complexity
# O(N), auxilliary Space required for storing data in queues.

# Constraints
#  1 <= Number of operations on the stack <= 100
#  1 <= Values in the stack <= 100

from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        # Add the element to queue1
        self.queue1.append(x)

    def pop(self):
        if not self.queue1:
            return None  # Stack is empty
        # Move all elements from queue1 to queue2 except the last one
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        # Remove and return the last element from queue1
        popped_element = self.queue1.popleft()
        # Swap the queues
        self.queue1, self.queue2 = self.queue2, self.queue1
        return popped_element

    def top(self):
        if not self.queue1:
            return None  # Stack is empty
        # Move all elements from queue1 to queue2 except the last one
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        # Get the last element from queue1
        top_element = self.queue1[0]
        # Move the last element back to queue1
        self.queue2.append(self.queue1.popleft())
        # Swap the queues
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def is_empty(self):
        return not self.queue1
