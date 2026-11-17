class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort the arrangement of the cars by their position 
        cars = sorted(list(zip(position , speed)), key = lambda x : x[0], reverse = True)

        fleet  = []
        #iterate through the cars and determine their fleet 
        for i , car in enumerate(cars):
            if not fleet:
                fleet.append([i])
                continue 
            #calculate current car final position
            position = car[0]
            speed = car[1]
            timeCar = (target - position) / speed
            #caluclate top fleet final position 
            top = cars[fleet[-1][0]]
            position = top[0]
            speed = top[1]
            timeFleet = (target - position) / speed
            #determine if the car belongs to top fleet or new fleet
            if timeCar <= timeFleet:
                fleet[-1].append(i)
            else:
                fleet.append([i])
        return len(fleet)


