class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #maintain a stack of indexes of the days 
        #when a warmer day is found, pop from the top, the number is i-stored index
        #stop popping when the current temperatures is lower than the top item
        from collections import deque
        results = [ 0 for i in range(len(temperatures))]
        stack = deque()

        for i , temp in enumerate(temperatures):
            while stack:
                if  temp > temperatures[stack[-1]]:
                    index = stack.pop()
                    results[index] = i - index
                else:
                    break
            stack.append(i)

        return results 