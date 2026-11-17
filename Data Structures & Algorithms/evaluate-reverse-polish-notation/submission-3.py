class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #read from the left to right , store the numbers into the stack
        #upon reading a operator, pop 2 number fom the stack to compute the result
        #then append the result onto the stack
        #retrieve the single item from the stack as the output
        from collections import deque
        stack = deque([])
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
                continue
            operand2 = stack.pop()
            operand1 = stack.pop()
            operator = token

            result = 0
            if operator == "+":
                result = operand1 + operand2
            elif operator == "*":
                result = operand1 * operand2
            elif operator == "/":
                result = int(operand1 / operand2)
            else:
                result = operand1 - operand2
            stack.append(result)
        return stack.pop()
        