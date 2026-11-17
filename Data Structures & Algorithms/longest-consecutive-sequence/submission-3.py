class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #put all number into a set for O(1) check for element existance
        #the intuition is that if a number doesnt have immediate left , it is a start of a sequence
        #access each number and check if its start of a sequence by looking left
        #if left exist then its not a start and so continue
        #if left doesnt exist and the right exist , then keep going until the right doesnt exist
        #update the count of the max sequence so far

        numset = set(nums)
        maxlen = 0
        for i in range(len(nums)):

            if nums[i]-1 in numset:
                continue

            start = nums[i]
            temp_counter = 1
            #since the while loop is only runned when a start of sequence is seen
            #so the activation of the while loop is less than n times and less than n iterations
            #so its more like O(n + kn) where k is smaller than n
            while start+1 in numset:
                temp_counter +=1
                start +=1
            if temp_counter > maxlen:
                maxlen = temp_counter
        return maxlen