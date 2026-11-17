class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #maintain a stack of indexes of the days 
        #when a warmer day is found, pop from the top, the number is i-stored index
        #stop popping when the current temperatures is lower than the top item
        
        result = [0  for i in range(len(temperatures))]
        from collections import deque
        stack = deque()
        for i in range(len(temperatures)):
            current = temperatures[i]
            while stack and current > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result

        
        