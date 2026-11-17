class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        indices = 0
        result = [0 for j in temperatures]
        for i in range(len(temperatures)):
            val = temperatures[i]
            if not stack:
                stack.append(i)
            elif val >temperatures[stack[-1]]:

                while stack and val > temperatures[stack[-1]]:
                    v = stack.pop()
                    result[v] = i-v
                
                stack.append(i)
            else:
                stack.append(i)
        return result


                

                 