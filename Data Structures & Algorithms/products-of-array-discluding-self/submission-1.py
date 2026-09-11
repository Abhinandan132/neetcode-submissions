class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Naive approach. 
        zeroCnt, product = 0, 1
        for num in nums: 
            if (num): 
                product *= num 
            else: 
                zeroCnt += 1
        if (zeroCnt  > 1):
            return [0] * len(nums)
        product_array = [0] * len(nums)
        for i, num in enumerate(nums): 
            if (zeroCnt): product_array[i] = 0 if num else product 
            else: product_array[i] = product // num
        return product_array
        