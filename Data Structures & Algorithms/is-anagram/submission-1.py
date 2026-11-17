class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if len is different that its not 
        if len(s)!=len(t):
            return False
        #use a hash map to store frequency of chars
        from collections import defaultdict
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for char in s:
            s_dict[char]+=1
        for char in t:
            t_dict[char]+=1
        
        if s_dict != t_dict:
            return False
        return True