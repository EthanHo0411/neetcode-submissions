class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #since we want to get the top k frequent numbers in the list
        #we need to first determine their frequency and rank them 
        #a good approach to do this in O(n) is bucket sort
        #so we first create n buckets where n is the length of the list
        #the intuition is that a number can at least appear n times
        #then we creat a hashmap to count the frequency of each number in O(n)
        #we then iterate through these numbers and place them in the correct bucket according to their frequency
        # for example , if the number appears once, it belongs to the bucket at index 1
        #at this point , we would have attained a ranking of the number's frequency in ascending order
        #thus , starting from the end , we can pop the numbers from the buckets one by one
        #until we have k numbers 
        #these numbers are the top k frequency numbers


        from collections import defaultdict
        frequency = defaultdict(int)
         #initialise number of bucket equal to the number of numbers
        buckets = [[] for i in range(len(nums)+1)]
         #count the frequency of each number
        for num in nums:
            frequency[num] +=1

         #put the number into their bucket based on frequency
        for key in frequency.keys():
            buckets[frequency[key]].append(key)
        
        result = []
        i = len(nums)
        #keep appending the bucket until meeting k
        while len(result)<k:
            if len(buckets[i]) == 0:
                i -=1
            else:
                result.append(buckets[i].pop())
        return result