ALICE = True
BOB = False


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = 0
        winner = ALICE
        vowel_count = []
        vowel_index = {}


        VOWEL_SET = set("aeiou")
        for i, e in enumerate(s):
            if e in VOWEL_SET:
                count += 1
            if count not in vowel_index:
                vowel_index[count] = i

            vowel_count.append(count)

        
        print(vowel_count)
        if count == 0:
            return BOB
        else:
            return ALICE
        

        

