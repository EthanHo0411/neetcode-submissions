class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dicct = {}
        for word in strs:
            x = word
            new = ''.join(sorted(x))
            if new not in dicct:
                dicct[new] = [word]
            else:
                dicct[new].append(word)
        return list(dicct.values())