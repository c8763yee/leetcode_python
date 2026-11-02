from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        size = len(tickets)
        tickets = deque(tickets)
        index = 0
        count = 0
        while True:
            if tickets[0] > 0:
                tickets[0] -= 1
                count += 1
                if tickets[0] == 0 and index == k:
                    break

            index = (index + 1) % size
            tickets.rotate(-1)

        return count