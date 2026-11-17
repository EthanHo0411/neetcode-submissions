class Solution:

    #use the format of <string length> <some symbol> <actual string>
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
