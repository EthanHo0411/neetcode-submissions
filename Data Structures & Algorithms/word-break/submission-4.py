class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #base case reaching the end
        cache = {len(s): True}

        #we are trying to see if there are any word that starts from this index 
        #and we can segment the rest from that index
        def dfs(i):

            #if its already feasible from that index
            if i in cache:
                return cache[i]

            #iterate through the words to see which word can be used from this index
            #then see if we use this word, is it possible to segment the rest from the ending index
            #if yes, it means we can segment the substring from this index

            for w in wordDict:
                if i + len(w) <=len(s) and s[i:i+len(w)] == w:
                    if dfs(i+len(w)):
                        cache[i] = True
                        return True 
            cache[i] = False
            return False
        return dfs(0)           
            
