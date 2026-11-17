class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #dp top bottom approach
        #go diagonal if its the same , else go right or down
        #for example, for abc and dbc , explore (abc,bc) or (db,bc) , see which one have a longer subsequence


        #initialize the 2D array with one extra column for the zero length of both sequence
        #used for building up the matrix
        dp = [ [ 0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        #starting from the end of both string and slowly build backward
        for i in range(len(text1)-1, -1 , -1):
            for j in range(len(text2)-1, -1 ,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 +dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],  dp[i][j+1])
        return dp[0][0]