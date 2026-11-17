class Solution:
    def isValid(self, s: str) -> bool:
        #use a deque to append and pop the brackets
        #store the opening brackets and pop them when a closing one is seen
        #if the open and close doesn't match , its invalid
        from collections import deque 
        q = deque()
        dictt = {"(":")","[":"]","{":"}"}
        for b in s: 
            if b in dictt: 
                q.append(b)
            else: 
                if not q or b != dictt[q[-1]]:
                    return False
                else:
                    q.pop()
        return True if not q else False
        
            