class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def finish(k):
            import math
            total = 0
            for pile in piles: 
                total += math.ceil(pile/k)
            return total <= h

        #find the boundary for k , then perform binary search 
        upper = max(piles)
        lower = 1

        #perform binary search on the best k 
        #conditioned on if all the bananas can be finished within h hours
        #try to be as small as possible 
        l , r = lower , upper
        
        while l < r:
            mid = l + (r-l)//2
            
            if finish(mid):
                r = mid 
            else:
                l = mid + 1
        return l
        