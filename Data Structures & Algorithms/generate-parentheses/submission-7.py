class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #backtracking method where a path would be explored, then changes undone to explore another 
        #the number of open >= close & cannot start with a close
        #at each step explore the open and close option by recursive call and popping from stack 
        result = []
        def backtracking(pattern : List[str] , o :int , c:int):

            #base case , implies the the pattern is complete
            if o == c == n:
                result.append("".join(pattern))
                return 
            temp = pattern
            #add a open if its less than n
            if o<n:
                temp.append("(")
                backtracking(temp,o+1, c)
                temp.pop()
            #test the case where open > close, can have another close
            if o>c:
                temp.append(")")
                backtracking(temp, o, c+1)
                temp.pop()
                            
            

        backtracking(deque(),0, 0)
        return result

