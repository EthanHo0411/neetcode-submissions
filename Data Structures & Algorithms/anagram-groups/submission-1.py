class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dicct = defaultdict(list)
        for word in strs:
            new = ''.join(sorted(word))
            dicct[new].append(word)
        return list(dicct.values())