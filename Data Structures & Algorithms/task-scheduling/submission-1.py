class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #use counter to record the number of occurence of the char
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        import heapq
        heapq.heapify(maxheap)
        time = 0 
        q = deque()
        while maxheap or q:
            time+=1
            if not maxheap:
                time = q[0][1]
            else:
                cnt = 1+ heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time