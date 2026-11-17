class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #first figure out the freq of char and the length of the string 
        from collections import defaultdict 
        freq = defaultdict(int)
        for s in s1:
            freq[s]+=1
        ls = len(s1)

        #loop thorugh s2 to search for the permutation
        l = 0
        tempf = defaultdict(int)
        noChar = len(freq.keys())
        counter = 0
        for i , s in enumerate(s2):

            tempf[s]+=1
            if i-l+1 > ls:
                left = s2[l]
                if left in s1 and tempf[left] ==  freq[left]:
                    counter -= 1
                tempf[s2[l]] -= 1
                l+=1
            #check if char count meets the requirement
            if s in s1 and tempf[s] == freq[s]:
                counter += 1
            if counter == noChar:
                return True
        return False
        
                