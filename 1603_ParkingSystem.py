class ParkingSystem1:

    def __init__(self, big: int, medium: int, small: int):
        self.park = {1:[big,0], 2:[medium,0], 3:[small,0]}

    def addCar(self, carType: int) -> bool:
        if carType in self.park and self.park.get(carType)[1] < self.park.get(carType)[0]:
            self.park[carType][1] += 1
            return True
        else:
            return False
        
class ParkingSystem:        
        
    def __init__(self, big, medium, small):
        self.A = [big, medium, small]

    def addCar(self, carType):
        self.A[carType - 1] -= 1
        return self.A[carType - 1] >= 0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)