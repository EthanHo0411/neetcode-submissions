class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0
        
        #store the index of the chars in the hashmap
        #the legnth is the diff between the current index (r) and left pointer ( the start)
        
        for i ,char in enumerate(s):
            if char in mp:
                l = max(mp[char]+1,l)
            mp[char] = i
            res = max(res, i-l+1)    
        return res