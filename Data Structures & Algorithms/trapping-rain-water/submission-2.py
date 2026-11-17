class Solution:
    def trap(self, height: List[int]) -> int:

        #the intuition is that the amount trapped at each index is determined by
        #the min of the max height from both its left and right
        #so as long as max left is < or same as the max right , the water trapped can be determined with the left alone
        #and as long as the left is > than the right, it means that its determined by the max right
        #jump between the two end using this theory until l pointer passes the r pointer
        if not height:
            return  0
        
        l,r = 0 , len(height)-1
        maxl, maxr = height[l], height[r]
        maxtrap = 0
        while l<r: 
            #if the maxr >maxl
            if maxr >=maxl:
                #move to the next bar
                l +=1
                #update the maxl
                maxl = max(maxl, height[l])
                maxtrap += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                maxtrap += maxr - height[r]
        return maxtrap

        