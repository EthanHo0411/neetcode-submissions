class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #perform bucket sort 
        #first record the frequency of the characters inside dictionary 

        from collections import defaultdict 
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1

        #create the buckets, one for each freq, including 0 index
        # the size maximum is determiend by the size of the list

        buckets = [[] for i in range(len(nums)+1)]
        #then place the characters into their corresponding bukcet index by frequency 

        for num in freq.keys():
            buckets[freq[num]].append(num)

        #append the number to the result list from the end 

        result = []
        i = 0 
        j = len(buckets)-1

        while i < k: 
            if not buckets[j]:
                j -=1
                continue

            result.append(buckets[j].pop())
            i+=1 
        return result