class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort the string to get a common key to select the group 
        #add the string to that group
        #return the list of values of the dictionary 

        from collections import defaultdict 
        result = defaultdict(list)
        
        for strings in strs:
            key = "".join(sorted(strings))
            result[key].append(strings)
        return list(result.values())
