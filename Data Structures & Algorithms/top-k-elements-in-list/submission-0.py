class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_nums = set(nums)
        from collections import defaultdict
        frequency = defaultdict(int)
        bucket = [[] for _ in range(len(nums)+1)]

        for num in nums:
            frequency[num]+=1
    
        for num in unique_nums:
            bucket_number = frequency[num]
            bucket[bucket_number].append(num)
        
        result = []
        index = len(bucket)-1

        while len(result) < k:
            if bucket[index]:
                result.append(bucket[index].pop())
            else:
                index-=1
        
        return result