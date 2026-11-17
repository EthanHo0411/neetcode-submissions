class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0
        
        #store the index of the chars in the hashmap
        #the legnth is the diff between the current index (r) and left pointer ( the start)
        
        for i ,char in enumerate(s):
            #if the char is already in the sliding window
            #update the start
            #to the max of (next position of the duplicated char, current l)
            #this is because if the current l is larger, it implies it already hadnled some duplicates
            if char in mp:
                l = max(mp[char]+1,l)
            #record the char position
            mp[char] = i
            res = max(res, i-l+1)    
        return res