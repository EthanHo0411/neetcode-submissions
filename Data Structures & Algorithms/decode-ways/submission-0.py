class Solution:
    def numDecodings(self, s: str) -> int:
        #create the memo and the base case for decoding
        dp ={len(s):1}

        #the function returns the number of decoding starting at index i
        def dfs(i):

            #base case
            #if its computed , return directly
            if i in dp:
                return dp[i]
            #if the digit is 0 return 0
            if s[i] == '0':
               return 0 
            
            #start decoding just a single digit
            #the idea is to think of it as ,when we are doing a single digit
            #whats the next one we need to call
            #the way we call the dfs already determines how many ways to split it according to the current plan
            #in this case since we are splitting a single digit, so the next one to call would be i +1
            res = dfs(i+1)

            #if the next digit is still smaller than the length, we can call another for two digit
            if i+1<len(s) and (s[i] == "1"or s[i] == "2" and s[i+1] in "0123456"):
                res+= dfs(i+2)
            
            dp[i] =  res
            return res
        return dfs(0)