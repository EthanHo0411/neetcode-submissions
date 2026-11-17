class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #use a hashmap to keep track of the highest count char in the sliding window
        #at each iteration check if (r-l+1) - maxf >k
        #if yes , it implies we need to shift the left pointer until this is no longer true
        #if no , we can keep incrementing the right pointer (i)
        from collections import defaultdict
        f = defaultdict(int)
        res = 0
        l = 0
        #iterate through the chars
        for i in range(len(s)):
            f[s[i]] +=1
            maxf = max(list(f.values()))

            while (i-l+1)-maxf >k:
                f[s[l]] -=1
                l +=1
            res = max(res, i-l+1)
        return res
