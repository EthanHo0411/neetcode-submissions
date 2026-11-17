class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #realise the lower bound 1 and upper bound the max pile, of k 
        #do binary search on the value of k
        #if the current k can eat all , then shift it to smaller
        #if the current k cnt eat all, make it bigger 
        #once we reach the part of k that can eat all, we keep going to the left until we can no longer eatall\
        import math
        def eatall(k):
            result = 0
            for pile in piles:
                result += math.ceil(pile/k)
            return result <=h
        
        l, r = 1, max(piles)
        
        while l<r:
            mid = l + ((r-l)//2)
            #we shift the right pointer to the mid to preserve the min eating speed
            if eatall(mid):
                r = mid
            else:
                l = mid+1
        return l
