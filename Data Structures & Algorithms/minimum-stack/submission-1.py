class MinStack:
#We can use a stack to maintain the elements. But how can we find the minimum element at any given time? Perhaps we should consider a prefix approach.
    from collections import deque
    def __init__(self):
        #use one stack for storing the min items
        self.minimum = deque([])
        #one stakc for storing all the items
        self.stack = deque([])
        #store the min value so far
        self.min_val = float("inf") 

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_val:
            self.min_val = val
        self.minimum.append(self.min_val)

        return None

    def pop(self) -> None:
        val = self.stack.pop()
        val = self.minimum.pop()
        self.min_val = self.minimum[-1] if self.minimum else float("inf")
        
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val
