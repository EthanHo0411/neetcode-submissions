class Solution:
    def countSubstrings(self, s: str) -> int:
        #use dynamic programming thats builds the palindrome bottom up

        #create table for storing subresults
        n = len(s)
        dp = [[False]*n for i in range(n)]
        counts = 0

        #initialise the len 1 items
        for i in range(n):
            dp[i][i] = True
            counts +=1 
        
        #explore palindrome with length 2
        #except the last one because we are checking for future one as well
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                counts+=1
        
        #explore the palindrome with len >=3 until n
        for length in range(3,n+1):
            for i in range(n-length+1):
                #figure out the ending index of the current window
                j = i+length-1

                if s[i] == s[j] and dp[i+1][j-1]:
                    #the current window is a valid palindrome
                    dp[i][j] =True
                    counts+=1
        return counts