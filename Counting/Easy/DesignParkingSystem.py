# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big > 0:
            self.big = self.big - 1
        elif carType == 2 and self.medium > 0:
            self.medium = self.medium-1
        elif carType == 3 and self.small > 0:
            self.small = self.small-1
        else:
            return False
        return True


obj = ParkingSystem(1, 1, 0)
print(obj.addCar(1))
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))
