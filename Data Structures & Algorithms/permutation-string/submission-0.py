class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #get a frequency hashmap for the s1
        #do slide windows for s2 and start comparing once reach the length of s1
        #shrink if the size is > s1

        if len(s1)>len(s2):
            return False
        from collections import defaultdict

        #create s1 dict
        f1 = defaultdict(int)
        for x in s1:
            f1[x] +=1
        
        #create s2 dict
        f2 = defaultdict(int)
        
        n = len(s1)
        l = 0
        #iterate through s2
        for i in range(len(s2)):
            f2[s2[i]] +=1 
            if i-l+1 > n:
                f2[s2[l]] -= 1
                if f2[s2[l]] == 0:
                    del f2[s2[l]]
                l +=1
            if i-l+1 == n:
                if f1 == f2:
                    return True
        return False

