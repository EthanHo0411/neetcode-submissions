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


        #get the unqiue numbers for bucket assigning later
        unique_nums = set(nums)
        from collections import defaultdict
        frequency = defaultdict(int)
        #initialise number of bucket equal to the number of numbers
        bucket = [[] for _ in range(len(nums)+1)]

        #count the frequency of each number
        for num in nums:
            frequency[num]+=1

        #put the number into their bucket based on frequency
        for num in frequency.keys():
            bucket_number = frequency[num]
            bucket[bucket_number].append(num)
        
        result = []
        index = len(bucket)-1
        #keep appending the bucket until meeting k
        while len(result) < k:
            if bucket[index]:
                result.append(bucket[index].pop())
            else:
                index-=1
        
        return result