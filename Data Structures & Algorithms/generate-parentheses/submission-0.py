class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #mean idea is that the closeN < openN
        #which eliminates most branches
        #recursion and then append to global res
        #the stack is used globally
        """Let's trace through a simple example where n=2:
Starting with backtrack(0, 0):

Add "(" → backtrack(1, 0)

Add "(" → backtrack(2, 0)

Add ")" → backtrack(2, 1)

Add ")" → backtrack(2, 2)

We have 2 open and 2 closed parentheses: add "(())" to result


Pop ")" and backtrack


Pop ")" and backtrack


Pop "(" and backtrack
Add ")" → backtrack(1, 1)

Add "(" → backtrack(2, 1)

Add ")" → backtrack(2, 2)

We have 2 open and 2 closed parentheses: add "()()" to result


Pop ")" and backtrack


Pop "(" and backtrack


Pop ")" and backtrack


Pop "(" and backtrack

Final result for n=2: ["(())", "()()"]"""
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res