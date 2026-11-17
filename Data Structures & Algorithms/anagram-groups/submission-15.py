class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort the string to get a common key to select the group 
        #add the string to that group
        #return the list of values of the dictionary 
        from collections import defaultdict 
        results = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            results[key].append(word)
        return list(results.values())