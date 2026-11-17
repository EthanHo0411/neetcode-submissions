class Solution:
#the key idea is to create a solution that would allow all types of char in teh string
#preserve the length of the string , then add a delimeter, then the actual stirng
#this format ensures correct reconstruction of the string 
    def encode(self, strs: List[str]) -> str:
        strings = []
        for x in strs:
            length = str(len(x))
            strings.append(length)
            strings.append("#")
            strings.append(x)
        return "".join(strings)
    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        length = ""
        result = []
        while i < len(s):
            if s[i] == "#":
                size = int(length) 
                length = ""
                i += 1
                result.append(s[i:i+size])
                i+= size
            else:
                length += s[i]
                i+=1

        return result