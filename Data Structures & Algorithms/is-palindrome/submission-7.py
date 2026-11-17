class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first filter out the blank space and the different non alphabetical chars
        #convert the char to lowercase
        filtered = [ char.lower() for char in s if char.isalnum() ]
        l = 0
        r = len(filtered)-1
        while l<r:
            if filtered[l] != filtered[r]:
                return False
            l +=1
            r -=1
        return True
