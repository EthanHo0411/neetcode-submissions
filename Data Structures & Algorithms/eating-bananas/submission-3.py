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
        
        # < is used here because we want to find the minimum , which is l
        # we already know the max (r) would work, so doing <= will make us find l == r 
        while l < r:
            
            mid = l + (r-l)//2
            #if we can finish it , mid could work, but we want to explore smaller values if there exist one            
            if finish(mid):
                r = mid 
            else:
                l = mid + 1
        #we know both l and r could work, but to find the min , we use l 
        return l
        