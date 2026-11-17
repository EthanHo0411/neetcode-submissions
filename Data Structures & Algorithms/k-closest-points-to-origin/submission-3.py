class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        import heapq
        
        def distance(point):
            return point[0]**2 + point[1]**2  # No need for sqrt - comparing squares is sufficient
        
        # Use a max heap to maintain k closest points
        # We'll use negative distances for a max heap
        max_heap = []
        
        for point in points:
            dist = distance(point)
            
            # If heap has less than k elements, just add the point
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist, point))
            else:
                # If this point is closer than the farthest point in the heap
                if dist < -max_heap[0][0]:
                    # Remove the farthest point and add this one
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-dist, point))
        
        # Extract the points from the heap
        return [point for _, point in max_heap]