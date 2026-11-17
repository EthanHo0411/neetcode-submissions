class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #initialisation
        cache = [[-1]*n for i in range(m)]

        def dfs(i,j):
            #base case reaching the goal
            if i == m-1 and j == n-1:
                return 1
            #if its in cache
            if cache[i][j] != -1:
                return cache[i][j]
            
            #recurrence , checking the total number of ways if we go right or down
            res= 0
            #check if we can go right
            if j < n-1:
                res+= dfs(i , j+1)
            #check if we can go down
            if i < m -1:
                res += dfs(i+1,j)
            
            cache[i][j] = res
            return res
        return dfs(0,0)
