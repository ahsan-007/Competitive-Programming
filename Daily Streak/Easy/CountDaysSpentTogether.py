# https://leetcode.com/problems/count-days-spent-together/description/?envType=daily-question&envId=2026-10-24

from datetime import datetime


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arrive_alice_dt = datetime.strptime(arriveAlice, "%m-%d")
        leave_alice_dt = datetime.strptime(leaveAlice, "%m-%d")

        arrive_bob_dt = datetime.strptime(arriveBob, "%m-%d")
        leave_bob_dt = datetime.strptime(leaveBob, "%m-%d")

        if arrive_alice_dt <= arrive_bob_dt <= leave_alice_dt:
            min_leave_dt = min(leave_bob_dt, leave_alice_dt)
            return (min_leave_dt - arrive_bob_dt).days + 1
        elif arrive_alice_dt <= leave_bob_dt <= leave_alice_dt:
            max_arrival_dt = max(arrive_alice_dt, arrive_bob_dt)
            return (leave_bob_dt - max_arrival_dt).days + 1
        elif arrive_bob_dt <= arrive_alice_dt <= leave_bob_dt:
            min_leave_dt = min(leave_alice_dt, leave_bob_dt)
            return (min_leave_dt - arrive_alice_dt).days + 1
        elif arrive_bob_dt <= leave_alice_dt <= leave_bob_dt:
            max_arrival_dt = max(arrive_alice_dt, arrive_bob_dt)
            return (leave_bob_dt - max_arrival_dt).days + 1
        return 0


print(Solution().countDaysTogether(arriveAlice="08-15",
      leaveAlice="08-18", arriveBob="08-16", leaveBob="08-19"))
print(Solution().countDaysTogether(arriveAlice="10-01",
      leaveAlice="10-31", arriveBob="11-01", leaveBob="12-31"))
