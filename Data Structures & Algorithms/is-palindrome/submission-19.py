class Solution:
    def isPalindrome(self, s: str) -> bool:
        #have two pointer at both end coming to the centre
        #skip any non-alnum char and spaces along the way
        #if the lowercase of the char doesnt match, its not a palindrome
        #loop until the pointer passes each other
        #keep point is that the palindrome can be odd and even length
        # the odd case have to be handled by using i<=j , where i or j could be equal to eachother at the centre
        i = 0 
        j = len(s)-1

        while i <= j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue 
            #check if its the same char 
            if s[i].lower() != s[j].lower():
                return False
            i+=1 
            j-=1
            
        return True