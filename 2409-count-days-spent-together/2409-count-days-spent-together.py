
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)
        return max(0, int(end[0:2]) * 100 + int(end[3:]) - int(start[0:2]) * 100 - int(start[3:]) + 1) if start[:2] == end[:2] else self.days(start, end)
    
    def days(self, start: str, end: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def day(s):
            m, d = int(s[:2]), int(s[3:])
            return sum(months[:m-1]) + d
        return max(0, day(end) - day(start) + 1)
