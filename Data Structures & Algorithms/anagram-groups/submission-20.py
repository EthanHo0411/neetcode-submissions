class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort the string to get a common key to select the group 
        #add the string to that group
        #return the list of values of the dictionary 
        from collections import defaultdict 

        groups = defaultdict(list)

        for string in strs: 
            key = "".join(sorted(string))
            groups[key].append(string)
        return list(groups.values())
