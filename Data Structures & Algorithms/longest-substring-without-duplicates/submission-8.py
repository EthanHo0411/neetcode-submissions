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
            #this is to make sure its not going backward 
            #this way it naturally tracks the largest window , moves l only when it has t
            if char in mp:
                l = max(l, mp[char]+1)
            mp[char] = i
            res = max(res, i-l+1)
        return res
            