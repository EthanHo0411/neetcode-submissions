class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current,x,y,n):
            #base case
            if len(current) == 2*n:
                result.append(current)
                return
            
            #add open bracket to cover this two case
            #if open <n 
            #if the open bracket is equal to the close bracket
            if x<n:
                backtrack(current+"(" , x+1, y, n)

            #if the open bracket is more than the close bracket
            if x>y:
                backtrack(current+")",x,y+1,n)
            return
        
        #call the function starting with "("
        backtrack("(",1,0,n)
        return result
