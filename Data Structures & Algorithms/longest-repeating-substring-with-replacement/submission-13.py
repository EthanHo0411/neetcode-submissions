class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #replace the characters that has the least freq within a sequence
        #determine the most popular char in each sliding window 
        # figure out if maxf + k  <=total, meaning if its possible after k replacements
        #if its not possible, shrink the left side of the sliding window until it fits
        from collections import defaultdict
        l = 0
        i = 0
        freq = defaultdict(int)
        maxlen = 0
        for i in range(len(s)):
            freq[s[i]]+=1

            maxf = max(freq.values())

            while maxf + k < (i-l+1):
                freq[s[l]]-=1
                l+=1
            maxlen = max(maxlen , i-l+1)
        
        return maxlen