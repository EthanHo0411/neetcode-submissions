class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort the string to get a common key to select the group 
        #add the string to that group
        #return the list of values of the dictionary 
        from collections import defaultdict 
        anagrams = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            anagrams[key].append(string)
        return list(anagrams.values())