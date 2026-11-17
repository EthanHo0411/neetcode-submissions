class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # at each sliding window , there will only be one maximum 
        #when carried forward to the next sliding window, we compares to the current max
        #when the current max is out of the sliding windows range, search for the new max
        result = []
        queue = {}
        l = 0
        maxItem = float("-inf")
        while l+k <= len(nums):
            #handles initialisation & max is now out of range
            #search for the new max 
            if not queue: 
                #the index of the item indicates how many more times it could be considered the maximum
                window = nums[l:l+k]
                maxItem = max(window)
                queue[maxItem] = window.index(maxItem)
            else:
                #check if the current max is still within range
                queue[maxItem] -=1
                if queue[maxItem] == -1:
                    del queue[maxItem]
                    continue
                #update the new maxItem 
                newItem = nums[l+k-1]
                if newItem >= maxItem:
                    del queue[maxItem]
                    maxItem = newItem
                    queue[maxItem] = 2
                
            result.append(maxItem)
            l+=1    
        return result
        