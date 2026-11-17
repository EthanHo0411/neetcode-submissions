class Solution:
    def isPalindrome(self, s: str) -> bool:
        #have two pointer at both end coming to the centre
        #skip any non-alnum char along the way
        #loop until the pointer passes each other

        i = 0 
        j = len(s)-1

        while i <= j:
            
            if s[i] == " " or not s[i].isalnum():
                i+=1
                continue
            if s[j] == " " or not s[j].isalnum():
                j-=1
                continue
            
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True
                