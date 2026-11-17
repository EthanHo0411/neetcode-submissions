class Solution:
    def trap(self, height: List[int]) -> int:
        #rain water is trapped by a left and right column 
        #the amount trapped depends on the height of the shortest side
        #with this property we can deduce the rainwater trapped at each index
        #as long as with know the current column is smaller than some column on the other side
        #we can already deduce the water trapped is at most the height of the current column
        #the actual amount trapped is the current column height - next column height
        #move the pointer with the smaller height at each time to satisfy the property
        l = 0 
        r = len(height)-1
        total = 0

        maxl = 0
        maxr = 0
        while l<r:
            if height[l]<height[r]:
                maxl = max(maxl,height[l])
                total += max(maxl - height[l],0)
                l+=1
            else:
                maxr = max(maxr,height[r])
                total += max(maxr - height[r],0)
                r-=1
        return total
        