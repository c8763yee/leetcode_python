class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        count = 0
        # print(counter)
        for word in words:
            flag = 1
            for c in set(word):
                if c not in counter or word.count(c) > counter[c]:
                    flag = 0
                    break
            if flag:
                count += len(word)

        return count