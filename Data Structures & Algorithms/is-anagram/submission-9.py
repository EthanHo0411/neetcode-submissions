class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create two dictionary to store the frequency of the characters 
        #compare the dictionary at the end 
        #use defaultdict for auto initialisation to 0 
        from collections import defaultdict 

        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        if len(s)>len(t):
            return False

        for char in s:
            freq1[char]+=1
        for char in t:
            freq2[char]+=1
        
        return freq1 == freq2