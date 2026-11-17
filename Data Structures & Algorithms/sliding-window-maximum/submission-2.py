class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maintain a double sided deque that maintains the largest item 
        #compare the max item at each step and start appending when >= index k
        #the index is being stored to check if its out of range
        #the max is always at index 0
        result = []
        from collections import deque 
        q = deque()
        l = r = 0

        while r < len(nums):
            #compare and add maxitem to the deque 
            #use while here because there might be multiple same max
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #check for out of range maxes
            if l > q[0]:
                q.popleft()
            
            #store the result since index k-1
            if r+1 >= k:
                result.append(nums[q[0]])
                l+=1
            r+=1
        return result






        