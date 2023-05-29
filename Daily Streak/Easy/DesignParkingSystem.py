# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big = self.big - 1
            else:
                return False
        elif carType == 2:
            if self.medium > 0:
                self.medium = self.medium - 1
            else:
                return False
        else:
            if self.small > 0:
                self.small = self.small - 1
            else:
                return False
        return True


parkingSystem = ParkingSystem(1, 1, 0)
print(parkingSystem.addCar(1))
print(parkingSystem.addCar(2))
print(parkingSystem.addCar(3))
print(parkingSystem.addCar(1))
