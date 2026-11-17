class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #append items into the queue when its numbers
        #pop out operands for computation 
        #append the result back onto the stack 

        queue = deque()
        sett = {"+","-","*","/"}
        for token in tokens:
            if token not in sett:
                queue.append(token)
            else:
                op1 = int(queue.pop())
                op2 = int(queue.pop())

                if token == "+":
                    queue.append(op1+op2)
                elif token == "-":
                    queue.append(op2-op1)
                elif token == "*":
                    queue.append(op1*op2)
                else:
                    queue.append(int(op2/op1))
        return int(queue[0])