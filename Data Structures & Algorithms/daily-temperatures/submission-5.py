class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                index = stack.pop()[0]
                diff = i - index
                result[index] = diff

            stack.append([i,temperatures[i]])
        return result

                

                 