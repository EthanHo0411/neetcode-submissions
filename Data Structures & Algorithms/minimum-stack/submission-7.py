class MinStack:

    def __init__(self):
        #a queue for current item on the stack 
        self.q = []
        #a queue for the current min on the stack at each timing 
        self.minq = []
        #variable for the current min
        self.minn = float("inf")

    def push(self, val: int) -> None:
        self.q.append(val)
        self.minn = min(self.minn, val)
        self.minq.append(self.minn)

    def pop(self) -> None:
        self.q.pop()
        self.minq.pop()
        if self.minq:
            self.minn = self.minq[-1]
        else: 
            #reset the self.minn to prevent popped value being preserved
            self.minn = float("inf")

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.minn
