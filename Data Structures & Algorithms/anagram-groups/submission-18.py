class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort the string to get a common key to select the group 
        #add the string to that group
        #return the list of values of the dictionary 
        from collections import defaultdict 

        result = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            result[key].append(word)
        return list(result.values())
