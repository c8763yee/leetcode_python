class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        product = 1
        product_one = 0
        zero_count = 0
        product_list = [0 for i in nums]

        for i in nums:
            product *= i
            if i != 0:
                if product_one == 0:
                    product_one = i
                else:
                    product_one *= i

            else:
                zero_count += 1
            
            if zero_count == 2:
                return product_list

        for i in range(l-1, -1, -1):
            product_list[i] = product // nums[i] if product != 0 else product_one * (nums[i] == 0)
        
        return product_list