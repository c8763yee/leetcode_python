from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def is_valid_bouquet(target, m_bouquet, k_flower):
            bouquet_count = 0
            flower_count = 0
            
            for day in bloomDay:
                if day > target:
                    flower_count = 0
                    continue
                flower_count += 1
                if flower_count == k_flower:
                    bouquet_count += 1
                    flower_count = 0
                    if bouquet_count >= m_bouquet:
                        return True
            
            return bouquet_count >= m_bouquet

        size = len(bloomDay)
        if m * k > size:
            return -1
        min_ele = 0
        max_ele = 2 ** 31 - 1
        while min_ele < max_ele:
            mid = (max_ele + min_ele) // 2
            if is_valid_bouquet(mid, m, k):
                max_ele = mid
            else:
                min_ele = mid + 1
        
        if is_valid_bouquet(min_ele, m, k):
            return min_ele
        return -1
