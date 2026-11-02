class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        counts = [count 
                  for i in bank 
                  if (count:= i.count('1'))]

        size = len(counts)
        if size <= 1:
            return 0

        beams = 0
        for i in range(size-1):
            beams += counts[i] * counts[i+1]


        return beams