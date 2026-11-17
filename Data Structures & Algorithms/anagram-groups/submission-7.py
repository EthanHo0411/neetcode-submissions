class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort each string to find out the common key for them in the dict

        from collections import defaultdict 
        dictt = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            dictt[key].append(string)
        return list(dictt.values())