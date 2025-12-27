# https://leetcode.com/problems/meeting-rooms-iii/description/?envType=daily-question&envId=2025-12-27

from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])

        occupiedRooms = []
        unOccupiedRooms = list(range(n))
        heapify(unOccupiedRooms)

        def freeOccupiedRoomsTill(t):
            while occupiedRooms and t >= occupiedRooms[0][0]:
                _, roomNo = heappop(occupiedRooms)
                heappush(unOccupiedRooms, roomNo)

        roomMeetingCount = {}
        maxMeetingsCount = 0
        maxMeetingsRoomNo = 0

        currTime = 0
        for meeting in meetings:
            if (unOccupiedRooms and (not occupiedRooms or occupiedRooms[0][0] > currTime)) or (occupiedRooms[0][0] <= meeting[0]):
                currTime = max(currTime, meeting[0])
            else:
                currTime = max(occupiedRooms[0][0], currTime)

            freeOccupiedRoomsTill(currTime)
            roomNo = heappop(unOccupiedRooms)
            heappush(occupiedRooms, (currTime +
                                     meeting[1] - meeting[0], roomNo))

            roomMeetingCount[roomNo] = roomMeetingCount.get(roomNo, 0) + 1
            if roomMeetingCount[roomNo] > maxMeetingsCount or (roomMeetingCount[roomNo] == maxMeetingsCount and roomNo < maxMeetingsRoomNo):
                maxMeetingsCount = roomMeetingCount[roomNo]
                maxMeetingsRoomNo = roomNo

        return maxMeetingsRoomNo


print(Solution().mostBooked(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]]))
print(Solution().mostBooked(n=3,
                            meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))
print(Solution().mostBooked(n=2,
                            meetings=[[0, 10], [1, 2], [12, 14], [13, 15]]))
print(Solution().mostBooked(n=4,
                            meetings=[[19, 20], [14, 15], [13, 14], [11, 20]]))
print(Solution().mostBooked(n=4,
                            meetings=[[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]))
print(Solution().mostBooked(n=3,
                            meetings=[[3, 7], [12, 19], [16, 17], [1, 17], [5, 6]]))
