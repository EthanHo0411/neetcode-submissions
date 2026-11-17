class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque 

        brackets = {"}" : "{", "]": "[", ")":"("}
        stack = deque()
        close = brackets.keys()
        for bra in s:
            if bra in close:
                opens = brackets[bra]
                if stack and stack.pop() == opens:
                    continue 
                else:
                    return False
            stack.append(bra)
        return True if not stack else False
            