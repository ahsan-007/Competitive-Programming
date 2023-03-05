# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.record = {}
        self.check_ins = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        key = self.check_ins[id][0] + "->" + stationName
        if key not in self.record:
            self.record[key] = [0, 0]
        self.record[key][0] += 1
        self.record[key][1] += t - self.check_ins[id][1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return round(self.record[startStation + '->' + endStation][1] / self.record[startStation + '->' + endStation][0], 5)


system = UndergroundSystem()
system.checkIn(45, "Leyton", 3)
system.checkIn(32, "Paradise", 8)
system.checkIn(27, "Leyton", 10)
system.checkOut(45, "Waterloo", 15)
system.checkOut(27, "Waterloo", 20)
system.checkOut(32, "Cambridge", 22)
print(system.getAverageTime("Paradise", "Cambridge"))
print(system.getAverageTime("Leyton", "Waterloo"))
system.checkIn(10, "Leyton", 24)
print(system.getAverageTime("Leyton", "Waterloo"))
system.checkOut(10, "Waterloo", 38)
print(system.getAverageTime("Leyton", "Waterloo"))


system = UndergroundSystem()
system.checkIn(10, "Leyton", 3)
system.checkOut(10, "Paradise", 8)
print(system.getAverageTime("Leyton", "Paradise"))
system.checkIn(5, "Leyton", 10)
system.checkOut(5, "Paradise", 16)
print(system.getAverageTime("Leyton", "Paradise"))
system.checkIn(2, "Leyton", 21)
system.checkOut(2, "Paradise", 30)
print(system.getAverageTime("Leyton", "Paradise"))


# I have further modified the logic of comparison. Results are better than previous version. Updated version has been deployed.
