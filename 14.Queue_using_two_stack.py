# Implement a Queue using 2 stacks s1 and s2 . A Query Q is of 2 Types (i) 1 x (a query of this type means pushing 'x' into the queue) (ii) 2 (a query of this type means to pop element from queue and print the poped element)

# Sample Input
# 5
# 1 2 1 3 2 1 4 2
# Sample Output
# 2 3
# Sample Explanation
# In the first testcase
# 1 2 the queue will be {2}
# 1 3 the queue will be {2 3}
# 2   poped element will be 2 the queue will be {3}
# 1 4 the queue will be {3 4}
# 2   poped element will be 3.
# Expected Time Complexity
# O(1) for push() and O(N) for pop() or O(N) for push() and O(1) for pop()

# Expected Space Complexity
# O(N), auxilliary space required for to store data in stacks.

# Constraints
#  1 <= Q <= 100
#  1 <= x <= 100

# *
class MyQueue:
    def __init__(self):
        self.stack1 = []  # For enqueue operation
        self.stack2 = []  # For dequeue operation

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            # If stack2 is empty, transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return None  # Queue is empty

    def peek(self):
        if not self.stack2:
            # If stack2 is empty, transfer elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2[-1]
        else:
            return None  # Queue is empty

    def is_empty(self):
        return not self.stack1 and not self.stack2
