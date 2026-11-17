class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove non alphanumeric chars and change to lowercase
        #two pointer from both end and check until they pass eachother
        p1 = 0
        s = "".join(char.lower() for char in s if char.isalnum())
        p2 = len(s)-1
        while p1<p2:
            if s[p1] == s[p2]:
                p1 +=1
                p2 -=1
            else:
                return False
        return True