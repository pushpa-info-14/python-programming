class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix = [0] * 13
        for i in range(12):
            prefix[i + 1] = months[i] + prefix[i]

        def get_days(date):
            month = int(date[:2])
            days = int(date[3:])
            return prefix[month - 1] + days

        arrive_alice = get_days(arriveAlice)
        leave_alice = get_days(leaveAlice)
        arrive_bob = get_days(arriveBob)
        leave_bob = get_days(leaveBob)

        start = max(arrive_alice, arrive_bob)
        end = min(leave_alice, leave_bob)
        if start <= end:
            return end - start + 1
        else:
            return 0


s = Solution()
print(s.countDaysTogether(arriveAlice="08-15", leaveAlice="08-18", arriveBob="08-16", leaveBob="08-19"))
print(s.countDaysTogether(arriveAlice="10-01", leaveAlice="10-31", arriveBob="11-01", leaveBob="12-31"))
