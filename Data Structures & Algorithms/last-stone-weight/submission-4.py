class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap, stone*-1)
        while len(maxheap)>1:
            first = heapq.heappop(maxheap)
            second = heapq.heappop(maxheap)
            if first == second:
                continue
            heapq.heappush(maxheap,abs(first - second)*-1)
        return maxheap[0]*-1 if maxheap else 0
        