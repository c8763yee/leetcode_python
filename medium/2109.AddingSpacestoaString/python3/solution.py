class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        if spaces == []:
            return s

        spaces = deque(spaces)
        result = []
        for i, c in enumerate(s):
            if spaces and i == spaces[0]:
                result.append(' ')
                spaces.popleft()
            result.append(c)

        return "".join(result)