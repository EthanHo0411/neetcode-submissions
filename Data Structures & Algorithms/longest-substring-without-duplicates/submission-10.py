class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a dictionary to keep track of current substring char freqs 
        # whenever a char is present in the dict, theres a duplicate 
        # determine whether this char is still relevant to the current slide window 
        # update the left side of the sliding window to create a new unique string 


        freq = {}
        maxlen = 0
        l = 0 
        for i in range(len(s)):
            #duplicate is found
            if s[i] in freq:
                l = max(l,freq[s[i]]+1)
            freq[s[i]] = i
            maxlen = max(maxlen, i-l+1)
        return maxlen