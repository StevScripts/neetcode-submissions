"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)
        
        lastMeetingEnds = 0

        for meeting in intervals:
            if lastMeetingEnds > meeting.start:
                return False

            lastMeetingEnds = meeting.end
        
        return True
