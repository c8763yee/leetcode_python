class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0: 1}
        prefix = 0
        count = 0

        for e in nums:
            prefix += e

            # 查詢過去有多少個符合條件的前綴和
            count += prefix_map.get(prefix - k, 0)

            # TODO: 更新 prefix_map[prefix] 的出現次數
            prefix_map[prefix] = prefix_map.get(prefix, 0)+1

        return count