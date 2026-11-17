class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #approach that doesnt involve comparing dictionary, faster when large number of unique char is used
        if len(s1) > len(s2):
            return False
        #first figure out the freq of char and the length of the string 
        from collections import defaultdict 
        freq = defaultdict(int)
        tempf = defaultdict(int)
        ls = len(s1)
        for s in s1:
            freq[s]+=1
        noChar = len(freq.keys())
        l = 0
        counter = 0
        #loop thorugh s2 to search for the permutation
        for i , s in enumerate(s2):
            tempf[s]+=1
            if i-l+1 > ls:
                left = s2[l]
                if left in s1 and tempf[left] ==  freq[left]:
                    counter -= 1
                tempf[s2[l]] -= 1
                l+=1
            #check if char count meets the requirement
            if s in freq and tempf[s] == freq[s]:
                counter += 1
            if counter == noChar:
                return True
        return False
        
                