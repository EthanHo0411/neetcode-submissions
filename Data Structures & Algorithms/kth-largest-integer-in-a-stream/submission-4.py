class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap , self.k = nums, k
        #create the heap and only maintain k items
        import heapq
        heapq.heapify(self.heap)
        while len(self.heap)>self.k:
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        #push the item onto the heap
        heapq.heappush(self.heap,val)
        #remove excess item from heap
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)
        #return the kth but dont pop it
        return self.heap[0]