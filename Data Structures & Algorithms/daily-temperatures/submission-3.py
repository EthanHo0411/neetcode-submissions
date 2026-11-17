class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            
            current = temperatures[i]
            #if the current one is larger than the previous ones
            #pop all of them and determine the lengh
            while stack and current > temperatures[stack[-1]]:
                index = stack.pop()
                diff = i - index
                result[index] = diff
            #append the current for future checking
            stack.append(i)
        return result
        


                

                 