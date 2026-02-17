# https://leetcode.com/problems/binary-watch/description/?envType=daily-question&envId=2026-02-17

from typing import List


class Solution:
    # Simulate
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def bitsToTime(bits):
            hour = int("".join(bits[0]), 2)
            minute = int("".join(bits[1]), 2)
            return f"{hour}:{str(minute):0>2}" if hour < 12 and minute < 60 else ""

        def readBinaryWatchUtil(bits, turnedOn, i, j):
            if turnedOn == 0:
                time = bitsToTime(bits)
                return [time] if time else []

            if i > 1:
                return []

            combinations = []
            if j < len(bits[i]):
                combinations.extend(
                    readBinaryWatchUtil(bits, turnedOn, i, j + 1))
                bits[i][j] = '1'
                combinations.extend(readBinaryWatchUtil(
                    bits, turnedOn - 1, i, j + 1))
                bits[i][j] = '0'
                return combinations
            else:
                return readBinaryWatchUtil(bits, turnedOn, i + 1, 0)

        bits = [
            ['0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0']
        ]
        return readBinaryWatchUtil(bits, turnedOn, 0, 0)

    # Enumerate
    def readBinaryWatchV2(self, turnedOn: int) -> List[str]:
        timeReadings = []
        for i in range(1024):
            hour = i >> 6
            minute = int(bin(i)[-6:], 2) if hour > 0 else i
            if hour < 12 and minute < 60 and bin(i).count("1") == turnedOn:
                timeReadings.append(f"{hour}:{str(minute):0>2}")
        return timeReadings


print(Solution().readBinaryWatch(1))
print(Solution().readBinaryWatch(9))

print(Solution().readBinaryWatchV2(1))
print(Solution().readBinaryWatchV2(9))
