class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []
        n = len(nums) 
        for i in range(n): 
            if (i > 0 and nums[i] == nums[i - 1]): continue 
            l = i + 1; h = n - 1
            while(l < h): 
                sum = nums[i] + nums[l] +  nums[h]
                if (sum == 0): 
                    res.append([nums[i], nums[l], nums[h]])
                    l += 1
                    h -= 1
                    while(l < h and nums[l] == nums[l - 1]): l += 1
                    while(l < h and nums[h] == nums[h + 1]): h -= 1
                elif (sum < 0): l += 1
                else: h -= 1 
        return res