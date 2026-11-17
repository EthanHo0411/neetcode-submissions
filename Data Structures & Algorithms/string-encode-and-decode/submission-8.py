class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode in a way len + some delimeter + string with arbitrary char 
        # this way it avoids the need to dedicate a char for separation 
        # all char can be used for the string
        result = ""
        for string in strs: 
            length = str(len(string))
            result += length
            result += "#"
            result += string
        return result 

    def decode(self, s: str) -> List[str]:
        #parse the string char by char 
        #the char until the # is the length of the coming string 
        result = []
        i = 0
        length = "" 
        while i < len(s):
            if s[i] == "#":
                i+=1
                result.append(s[i:i+int(length)])
                i += int(length)
                length = ""
                continue
            length += s[i]
            i += 1
        return result 

