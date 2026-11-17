class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a dictionary to keep track of current substring char freqs 
        # whenever a char is present in the dict, theres a duplicate 
        # determine whether this char is still relevant to the current slide window 
        # update the left side of the sliding window to create a new unique string 

        from collections import defaultdict 
        #storing the largest index of the char
        chars = defaultdict(int)
        
        #pointer for the left side of the sliding window 
        l = 0 
        maxlen = 0 

        for i in range(len(s)):
            if s[i] in chars:
                l = max( l , chars[s[i]]+1)
            chars[s[i]] = i
            maxlen = max(maxlen, i-l+1)
        return maxlen
