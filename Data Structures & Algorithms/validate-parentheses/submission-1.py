class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = "[({"
        close_brackets = "])}"
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                index = close_brackets.index(bracket)
                if stack and stack[-1] == open_brackets[index]:
                    item = stack.pop()
                else:
                    return False
        return True if not stack else False