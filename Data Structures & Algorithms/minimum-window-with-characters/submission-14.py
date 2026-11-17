class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #first determine the length and freq of char in t
        #then implement sliding window, expand until substring is captured 
            #shrink the sliding window from the left to find min length 
        #when no more substring is found, keep expanding


        #use len for determining number of keys
        #enumerate before using index and value pair
        from collections import defaultdict 
        freq = defaultdict(int)
        tempf = defaultdict(int)
        for x in t:
            freq[x]+=1
        noChar = len(freq.keys())
        counter = 0 
        l = 0
        minstring = ""

        for i , char in enumerate(s):
            tempf[char] +=1 
            if char in freq and tempf[char] == freq[char]:
                counter +=1 
            while counter == noChar and l <=i:
                if minstring == "":
                    minstring = s
                #update the string with the min length 
                minstring = min(minstring, s[l:i+1], key = len)
                #shrink from the left 
                tempf[s[l]] -=1
                if s[l] in freq and tempf[s[l]] < freq[s[l]]:
                    counter -=1

                l += 1 


        return minstring
