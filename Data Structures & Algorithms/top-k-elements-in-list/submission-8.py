class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use the bucket sort approach
        #first count the freq of each number, store in hashmap 
        #according to the freq of the number, place them in that index of an 2D array
        #finally starting from the end , pop number from the bucket until we have k items

        from collections import defaultdict
        freq = defaultdict(int)

        for num in nums:
            freq[num] +=1

        buckets = [[] for i in range(len(nums)+1)]
        
        for key in freq.keys():
            index = freq[key]
            buckets[index].append(key)
        
        count = 0 
        i = len(buckets)-1
        results = []
        while i >=0 and count <k:
            if buckets[i]:
                count +=1 
                item = buckets[i].pop()
                results.append(item)
            else:
                i-=1
        return results


