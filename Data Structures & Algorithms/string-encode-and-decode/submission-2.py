class Solution:

    #we want to connect the strings together into one and separate them back into individual strings
    #the intuition is to figure out a format that would preserve the length and the characters of the string
    #so that we can use any char for the strings without needing to worry about a specific separator that is used to separate them
    #use the format of <string length> <some symbol> <actual string>
    #so that we would know the number of characters belonging to a single string after the symbol
    #it works even if the actual string contains the symbol as we know the length 
    
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))
            result += "#"
            result += s
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i <len(s):
            length = ""
            while s[i]!="#":
                length += s[i]
                i +=1
            length = int(length)
            
            #skip the symbol block
            i +=1

            #get the string from i to i + length
            result.append(s[i:i+length])
            i+=length
        return result
