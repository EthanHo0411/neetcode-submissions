from collections import defaultdict, deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #use a dynamic sliding window  and add chars to it
        #only add the target chars , record the index of the target chars
        #record matches of the current window to the target string after every recording
        #add chars until the window contains all the target chars at least once ( matches is the len of t)
        #record the length and then popleft from the deque
        #shrink the windows from this popped index until another target char
        #this way it reduces the sliding window from the left for the shortest window as possible
        #if the current sliding window no longer contain all the target chars
        #add chars to the sliding window from the right
        #repeat until end of the string

        from collections import defaultdict, deque
        #create the dict for the target string
        target = defaultdict(int)
        for x in t:
            target[x]+=1
        #create dict for the window
        window = defaultdict(int)
        #create the deque for storing the positions
        position = deque([])
        #for recording the exact min substring
        min_len = float("inf")
        min_start = 0
        #record number of matches
        matches = 0
        #number of matches
        numMatch = len(target.keys())
        for i , char in enumerate(s):

            #update the freq for only the target char
            #update the position 
            #update the number of matches optinally
            if char in target:
                window[char] += 1 
                position.append(i)

                if target[char] == window[char]:
                    matches +=1
            
            #once the number of matches is the same as target matches
            #and there is still target char to be shrinked
            #shrink the window to find shorter length window
            while matches == numMatch and position:
                #calculate current window len
                start = position[0]
                window_len = i - start +1

                #update the min window and min start
                if window_len < min_len:
                    min_len = window_len
                    min_start = start

                #shrink the window
                item = s[position.popleft()]

                #update the window freq and number of matches
                window[item] -=1
                if window[item]<target[item]:
                    matches -=1
                
        return s[min_start:min_start+min_len] if min_len != float("inf") else ""
                



