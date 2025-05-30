# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/?envType=daily-question&envId=2025-05-30

from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        currNode = node1
        node1_path = {currNode: 0}

        distance = 1
        while edges[currNode] != -1 and edges[currNode] not in node1_path:
            node1_path[edges[currNode]] = distance
            currNode = edges[currNode]
            distance = distance + 1

        minDistance = float("+inf")
        minDistanceNode = None

        currNode = node2
        distance = 0
        visited = set()
        while currNode != -1 and currNode not in visited:
            if currNode in node1_path:
                currMaxDistance = max(distance, node1_path[currNode])
                if currMaxDistance < minDistance:
                    minDistance = currMaxDistance
                    minDistanceNode = currNode
                elif currMaxDistance == minDistance and currNode < minDistanceNode:

                    minDistanceNode = currNode

            visited.add(currNode)
            distance = distance + 1
            currNode = edges[currNode]

        return minDistanceNode if minDistance != float("+inf") else -1


print(Solution().closestMeetingNode(edges=[2, 2, 3, -1], node1=0, node2=1))
print(Solution().closestMeetingNode(edges=[2, 2, 3, -1], node1=1, node2=0))
print(Solution().closestMeetingNode(edges=[1, 2, -1], node1=0, node2=2))
print(Solution().closestMeetingNode(edges=[2, 0, 0], node1=2, node2=0))
