class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0, len(nums), 3):
            subarray = []
            first_element_in_subarray = nums[i]
            for j in range(3):
                if nums[i+j] - first_element_in_subarray > k:
                    return []
            
                subarray.append(nums[i+j])
            result.append(subarray)

        return result
                
