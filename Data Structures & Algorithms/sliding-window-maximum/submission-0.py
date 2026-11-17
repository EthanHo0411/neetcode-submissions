class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        #the idea is to maintain a deque that would only contain the maximum element
        #if the element is outside the window pop it from deque
        #at each step, we pop element in the deque that is smaller than the current one as the never will be the max
        #we add the current on to the deque
        #if we are at index >= k-1 , we can add the maximum to the deque
        #since we pop off all element smaller than current one, the first item is always the max


        result = []
        #store indices of item
        dq = deque()

        for i in range(len(nums)):

            #remove any item that is out of the range of sliding window
            #we start from the 0 index as whatever that is smaller is already removed
            while dq and dq[0] <= i-k:
                dq.popleft()
            
            #pop element that is less than the current one
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            #add the current element to the deque
            dq.append(i)

            #if we are at index >= k-1, we start appending max
            if i >=k-1:
                result.append(nums[dq[0]])
        return result