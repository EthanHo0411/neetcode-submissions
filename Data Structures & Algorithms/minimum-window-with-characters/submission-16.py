class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #first determine the length and freq of char in t
        from collections import defaultdict 
        freq = defaultdict(int)
        sliding = defaultdict(int)
        for char in t:
            freq[char] += 1
        noChar = len(freq.keys())
        #sliding window left pointer and target counter 
        l = 0 
        counter = 0
        #initialise the result and min len variable
        minlen = float("inf")
        minIndex = 0
        result = ""

        #implement sliding window, expand until substring is captured 
            #shrink the sliding window from the left to find min length 
        #when no more substring is found, keep expanding
        for i , char in enumerate(s):
            #update freq of sliding window 
            sliding[char] +=1

            #update the counter 
            if char in t and freq[char] == sliding[char]:
                counter +=1

            #only start shrinking once the target freq of chars are met
            while counter == noChar: 
                #record the result substring with preference to earlier index as tiebreaker
                length = i - l +1 
                if minlen > length: 
                    minlen = length 
                    minIndex = l

                #shrinking from the left 
                left = s[l]
                if left in t and freq[left] == sliding[left]:
                    counter -= 1
                sliding[left] -= 1
                l+=1
            
        return result if minlen == float("inf") else s[minIndex: minIndex+minlen]

