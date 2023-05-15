class Solution:
    def compress(self, chars: list[str]) -> int:
        char_count = length = ptr1 = 0
        previous = chars[0]
        chars.append(' ')
        for ptr2, c in enumerate(chars):
            if c == previous:
                char_count += 1
                continue

            chars[ptr1] = previous
            char_size = 0
            previous = c
            length += 1
            if char_count > 1:
                char_size += int(math.log10(char_count)) + 1
                length += char_size
                for i in range(char_size):
                    chars[ptr1 + i + 1] = str(char_count)[i]

            char_count = 1
            ptr1 += char_size + 1
            chars[ptr1] = c

        return length
