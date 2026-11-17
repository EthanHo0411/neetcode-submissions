class Solution:
    def longestPalindrome(self, s: str) -> str:
        #use dynamic programming to build the palindrome from bottomup
        #first create a 2D table and initialise individual chars to be paliindrome
        #second check if doubles are palindomr
        #then for segments of >three, check if they are palindromes by using previously stored boolean
        #and we just have to check the left or right to know if its a palindrome

        #create the table
        n = len(s)
        dp = [[False for i in range(n)] for i in range(n)]
        #create start index and max len
        start_idx = 0
        max_len = 1

        #create all individual entries
        for i in range(n):
            dp[i][i] = True
            start_idx = i
        
        #check for length 2 palindrome
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start_idx = i
                max_len =2
        #check for length >3 until length n
        for length in range(3,n+1):
            #for each length , we need a starting index and ending index
            for start in range(n-length+1):
                #finding the end index of the window, which is part of the window length
                #start +i would exceed by 1, so we need to -1 to get the ending index
                j = start + length -1

                if s[start] == s[j] and dp[start+1][j-1]:
                    dp[start][j] = True
                    if length >max_len:
                        start_idx = start
                        max_len = length
        return s[start_idx : start_idx + max_len]
