class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #replace the characters that has the least freq within a sequence
        #determine the most popular char in each sliding window 
        # figure out if maxf + k  <=total, meaning if its possible after k replacements
        #if its not possible, shrink the left side of the sliding window until it fits
        from collections import defaultdict
        maxlen = 0 
        l = 0  
        freq = defaultdict(int)
        i = 0 
        while i < len(s):
            freq[s[i]] +=1 
            #determine maxf of current substring 
            maxf = max(freq.values())

            while maxf + k < (i-l+1):
                freq[s[l]]-=1
                l +=1
            maxlen = max(maxlen,i-l+1)    
            i +=1 
        return maxlen
