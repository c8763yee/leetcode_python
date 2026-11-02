class Solution:
    def compress(self, chars: list[str]) -> int:
        if not chars or len(chars) == 1:
            return len(chars)

        write_pointer = count = 0
        n = len(chars)

        alpha_table = {}
        count_table = {}
        for read_pointer, char in enumerate(chars):
            count += 1

            # Check for character change or end of list
            if read_pointer < n - 1 and char == chars[read_pointer + 1]:
                continue

            alpha_table[char] = alpha_table.get(char, 0) + 1 
            count_table[(char, alpha_table[char])] = count
            
            count = 0

        for (char, _), time in count_table.items():
            # write first char
            chars[write_pointer] = char
            write_pointer += 1

            # write remain digit
            if time == 1:
                continue

            for c in str(time):
                chars[write_pointer] = c
                write_pointer += 1  

        return write_pointer
