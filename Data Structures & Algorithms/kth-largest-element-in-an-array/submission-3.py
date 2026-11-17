class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        import heapq
        maxheap = [num*-1 for num in nums]
        heapq.heapify(maxheap)
        x = k-1
        while maxheap and x >0:
            heapq.heappop(maxheap)
            x-=1
        return maxheap[0]*-1
        
        