class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #if yes, append it into the existing stack as it forms a car fleet
        #else append a new stack with itself

        #sort the car position in descending order (enumerate to contain its speed)
        cars = list(zip(position, speed))
        cars.sort(reverse= True, key = lambda x: x[0])

        fleet = [[cars[0]]]
        for car in cars:
        #(target - position) /  speed = time taken to reach the end
        #use the time required to reach the position for comparision
        #calculate to see if the current car <= time required to reach position
            time = (target-car[0])/car[1]
            current_fleet = fleet[-1][0]
            time1 = (target - current_fleet[0]) / current_fleet[1] 
            if time <= time1:
                fleet[-1].append(car)
            else:
                fleet.append([car])
        return len(fleet)