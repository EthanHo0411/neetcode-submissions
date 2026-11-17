class Solution:
    def climbStairs(self, n: int) -> int:
        # #the fact that the current one depend only on the future two makes it 
        # #possible to keep track of only two variables and replace them
        # one, two = 1,1 
        # for i in range(n-1):
        #     one, two = two, one+two
        # return two

        #top down 
        cache = [-1]*n
        def dfs(i):
            #base case 
            #if i equals to n it returns 1, sayings it a valid way
            #otherwise its not and so return 0
            if i >= n:
                return i == n
            #if we have already computed this then reuse it directly
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]
        return dfs(0)
             
