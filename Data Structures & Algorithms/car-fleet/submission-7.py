class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort the arrangement of the cars by their position 
        cars = sorted(list(zip(position , speed)), key = lambda x : x[0], reverse = True)
        
        fleet = [cars[0]]
        for car in cars:
            #compute the current car time to reach target
            timeCar = (target-car[0]) / car[1]
            #compute the time for the top fleet 
            top = fleet[-1]
            timeFleet = (target - top[0]) / top[1]

            #compare and determine if new fleet is formed 
            if timeCar > timeFleet:
                fleet.append(car)
        return len(fleet)
            