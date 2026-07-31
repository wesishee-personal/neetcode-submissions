"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort meetings
        sorted_meetings = sorted(intervals, key = lambda x: x.start)
        for i, meeting in enumerate(sorted_meetings):
            if i < len(sorted_meetings)-1 and meeting.end > sorted_meetings[i+1].start:
                return False
            
        return True
                