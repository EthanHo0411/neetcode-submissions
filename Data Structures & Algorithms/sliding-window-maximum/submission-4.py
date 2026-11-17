class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maintain a double sided deque that maintains the largest item 
        #compare the max item at each step and start appending when >= index k
        #the index is being stored to check if its out of range
        #the max is always at index 0

        from collections import deque 

        q = deque()
        l = 0
        result = []

        for i , n in enumerate(nums):
            #update the queue, pop out number < current item 
            while q: 
                if nums[q[-1]] < n:
                    q.pop()
                else:
                    break
            q.append(i)

            #remove any item that is out of range
            while q[0] < l: 
                q.popleft()
            
            #starting appending result when the sliding window length reached k 
            length = i - l + 1 
            if length == k: 
                result.append(nums[q[0]])
                l += 1 
        return result



        