class Solution:
    def isValid(self, s: str) -> bool:
        #record a stack for appending the brackets
        #one a closing one is seen, start popping from the stack
        # if the one that's popped doesn't match or there is no item to pop
        #then its not valid
        #if after the end of the string , the stack is also empty
        #the string is valid 
        i = 0
        stack = []
        #dictionary for the pairs
        dictt = {'(': ')', '{':'}', '[':']'}
        #closings set for constant time check
        closings = set(dictt.values())
        while i <len(s):
            #add to stack if its not closing
            if s[i] not in closings:
                stack.append(s[i])
            else:
                #if the stack is empty its not valid
                if not stack:
                    return False
                item = stack.pop()
                #False if the item popped isnt the opening for the current closing
                if s[i] != dictt[item]:
                    return False
            i+=1
        return True if not stack else False
            