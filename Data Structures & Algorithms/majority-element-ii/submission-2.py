class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Naive approach: Use hashing. 
        n = len(nums)
        cnt_1, cnt_2 = 0, 0 
        ele_1, ele_2 = -1, -1 
        for i in range(len(nums)): 
            if (nums[i] == ele_1): cnt_1 += 1
            elif (nums[i] == ele_2): cnt_2 += 1
            elif (cnt_1 == 0): 
                ele_1 = nums[i] 
                cnt_1 += 1
            elif (cnt_2 == 0): 
                ele_2 = nums[i] 
                cnt_2 += 1
            else: cnt_1 -= 1; cnt_2 -= 1
        # Validate
        cnt_1, cnt_2 = 0, 0
        for num in nums: 
            if num == ele_1: cnt_1 += 1
            elif num == ele_2: cnt_2 += 1
        res = []
        if (cnt_1 > n//3): res.append(ele_1) 
        if (cnt_2 > n//3): res.append(ele_2) 
        return res