class Solution:
    def climbStairs(self, n: int) -> int:
        #the fact that the current one depend only on the future two makes it 
        #possible to keep track of only two variables and replace them
        one, two = 1,1 
        for i in range(n-1):
            one, two = two, one+two
        return two