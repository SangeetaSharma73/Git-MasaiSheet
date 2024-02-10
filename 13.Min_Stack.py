# Design a stack that supports push, pop, top, and retrieving the minimum element in constant O(1) time.
# Note : You need to implement these functions on the stack : push(x) — Push element x into the stack. pop() — Removes the element from top of the stack. top() — Get the top element. getMin() — Retrieve the minimum element in the stack in O(1) time
# Sample Input
# push(3)
# push(5)
# push(1)
# getMin()
# pop()
# getMin()
# Sample Output
# Output:     
#     1
#     3
# Sample Explanation
# Stack  = [3,5,1]
# getMin() -> 1
# After pop
# Stack = [3,5]
# getMin() -> 3
# Expected Time Complexity
# O(1), for each operation

# Expected Space Complexity
# O(1), Constant extra space
# Constraints
# 1 <= N <= 100000


#Using class-
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            top_element = self.stack.pop()
            if top_element == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]

#without class:-
st=[]
min_st=[]
def push(x):
    st.append(x)
    if not min_st or x<=st[-1]:
        min_st.append(x)

def Pop():
    if st:
        top_element=st.pop()
        if top_element==min_st[-1]:
            min_st.pop()
def top():
    if st:
        return st[-1]

def Min_Stack():
    if min_st:
        return min_st[-1]

    

        
