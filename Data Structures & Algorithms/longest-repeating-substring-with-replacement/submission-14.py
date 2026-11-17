class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #replace the characters that has the least freq within a sequence
        #determine the most popular char in each sliding window 
        # figure out if maxf + k  <=total, meaning if its possible after k replacements
        #if its not possible, shrink the left side of the sliding window until it fits

        from collections import defaultdict 
        freq = defaultdict(int)
        l = 0 
        maxlen = 0
        for i in range(len(s)):
            #expand the sliding window 
            freq[s[i]] += 1

            #max freq of a char of the current window 
            maxf = freq[max(freq , key = freq.get)]

            if maxf + k < (i - l + 1):
                # shrinking the window from the left until its replaceable
                freq[s[l]] -= 1
                l += 1
            #record the current length
            maxlen = max(maxlen, i - l + 1)
        return maxlen