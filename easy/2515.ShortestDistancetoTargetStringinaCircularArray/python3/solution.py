class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0

        left = right = startIndex
        count = 0
        size = len(words)
        for i in range(size // 2):
            left = (left - 1) % size
            right = (right + 1) % size
            count += 1

            if words[left] == target or words[right] == target:
                return count

        return -1