class Solution:
    def stringSequence(self, target: str) -> List[str]:
        text = ""
        result = []
        for c in target:
            for a in string.ascii_lowercase:
                result.append(text + a)
                if a == c:
                    text += a
                    break

        return result