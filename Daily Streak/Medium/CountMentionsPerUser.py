# https://leetcode.com/problems/count-mentions-per-user/description/?envType=daily-question&envId=2025-12-12

from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # sort by x[1], in case of same timestamp, OFFLINE before MESSAGE
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))

        users = {userId: {"mentions": 0} for userId in range(numberOfUsers)}
        allCount = 0
        for event in events:
            event_type = event[0]
            if event_type == "MESSAGE":
                timestamp, mentions = event[1:]
                timestamp = int(timestamp)

                if mentions == "ALL":
                    allCount += 1

                elif mentions == "HERE":
                    for userId in users:
                        if timestamp - users[userId].get("offline_timestamp", -60) >= 60:
                            users[userId]["mentions"] += 1
                else:
                    mentionedIds = [int(mention[2:])
                                       for mention in mentions.split(" ")]
                    for mId in mentionedIds:
                        users[mId]["mentions"] += 1

            elif event_type == "OFFLINE":
                timestamp, userId = int(event[1]), int(event[2])

                users[userId]["offline_timestamp"] = timestamp

        mentions = [0] * numberOfUsers
        for userId in users:
            mentions[userId] = users[userId]["mentions"] + allCount
        return mentions


print(Solution().countMentions(numberOfUsers=2, events=[
      ["MESSAGE", "10", "id1 id0"], ["OFFLINE", "11", "0"], ["MESSAGE", "71", "HERE"]]))
print(Solution().countMentions(numberOfUsers=2, events=[
      ["OFFLINE", "10", "0"], ["MESSAGE", "12", "HERE"]]))
