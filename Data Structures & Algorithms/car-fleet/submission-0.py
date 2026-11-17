class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #sort by descending position
        #add the car to the stack one by one
        #if the time taken for the current one to reach target <= the top one on the stack
        #dont do anything, as they belong to the same fleet 
        #if they are not , then add to the stack , implying a new car fleet
        # len of the stack is the number of fleet

        #zip the position and its corresponding speed
        pairs = list(zip(position, speed))

        #sort by descending position
        pairs.sort(key = lambda x : x[0],reverse = True)

        stack = []
        
        for pair in pairs:
            if not stack:
                stack.append(pair)
            time_current = (target-pair[0])/pair[1]
            time_top = (target-stack[-1][0])/stack[-1][1]

            if time_current > time_top:
                stack.append(pair)
        return len(stack)

