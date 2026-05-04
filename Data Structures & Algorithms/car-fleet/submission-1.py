class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleet = 1
        prevTime = (target - cars[0][0]) / cars[0][1]

        for i in range(1, len(cars)):
            currTime = (target - cars[i][0]) / cars[i][1]
            if currTime > prevTime:
                fleet += 1
            
                prevTime = currTime
        
        return fleet
