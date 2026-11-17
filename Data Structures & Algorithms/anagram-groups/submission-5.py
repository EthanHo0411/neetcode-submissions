class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #since we are grouping the anagrams into sublist
        #the intuition is to first define the key that would be used to group them 
        #so a hashmap with string as key and list as value would be used to accomplish such goal 
        #defaultdict is used here so to initialise all the list for later appending
        #first we iterate through each of the words in the list
        #if two words are anagrams , they would have the same sorted string
        #so we sort the word to get a common string that is used to identify a group of anagrams
        #we append the word to the list corresponding to this common string (the key) in the hashmap
        #finally we return the list of values of the hashamp

        from collections import defaultdict
        dictt = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            dictt[key].append(string)
        return list(dictt.values())