class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [[], []]
        lose = {}
        for winner, loser in matches:
            lose[winner] = lose.get(winner, 0)
            lose[loser] = lose.get(loser, 0) + 1

        for player, match_lose in lose.items():
            if match_lose > 1:
                continue

            answer[match_lose].append(player)
        answer[0].sort()
        answer[1].sort()
        return answer