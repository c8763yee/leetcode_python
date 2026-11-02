class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait = now = size = 0
        for (arrive, time) in customers:
            if now < arrive: # not arrive right now
                now = arrive
            else: # already arrived
                wait += now - arrive

            wait += time
            now += time
            size += 1
        return wait / size