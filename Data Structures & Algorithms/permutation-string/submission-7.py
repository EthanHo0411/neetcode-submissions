class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #first make sure that s1 is no longer than s2 
        if len(s1) > len(s2):
            return False 
        
        #extract the freq of the char and the length of s1 
        from collections import defaultdict 
        freq = defaultdict(int)
        for char in s1:
            freq[char] += 1
        length = len(s1)
        #setup the counter for gradual comparison and the unique chars
        noChar = len(freq.keys())
        counter = 0 
        #the left pointer of the sliding window
        l = 0 
        # a dict for sliding window freq
        freq1 = defaultdict(int)
        #one pass through s2 to determine permutation  
        for i , s in enumerate(s2):

            #update the sliding window freq
            freq1[s] += 1
            #when sliding window length is larger than permutation length 
            if i-l+1 > length:
                # shrink the sliding window from the left and update conuters
                left = s2[l]
                if left in s1 and freq[left] == freq1[left]:
                    counter -=1
                freq1[left]-=1
                l+=1
            #update the counter if the char meets the target freq 
            if s in s1 and freq[s] ==  freq1[s]:
                counter += 1
            
            #if all chars freq meets the target freq then its found 
            if counter == noChar:
                return True
        return False

                