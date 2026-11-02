

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = deque()
        while deck:
            result.rotate()
            result.appendleft(deck.pop())

        return list(result)