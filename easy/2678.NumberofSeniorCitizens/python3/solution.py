class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        return sum(map(lambda detail:int((int(detail[11]) * 10 + int(detail[12]))>60), details))
