class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #hashmap for storing number of steps to target
        memo = {}

        def dfs(amount):

            #base case
            #if it is the amount needed
            if amount == 0:
                return 0
            #if it is already computed
            if amount in memo:
                return memo[amount]
            
            #for each of the coin value available
            #calculate the steps it takes to the target amount
            #make sure the amount after the coin is still positive or at least not negative
            res = min([1+ dfs(amount-coin) for coin in coins if amount-coin >=0]+[1e9])
            #record for later
            memo[amount] = res
            return res 
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins
            
