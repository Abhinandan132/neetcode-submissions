class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort() 
        res = [] 
        n = len(nums) 
        for i in range(n - 3): 
            if (i > 0 and nums[i] == nums[i - 1]): continue 
            for j in range(i + 1, n - 2): 
                if (j > i + 1 and nums[j] == nums[j - 1]): continue 
                l, h = j + 1, n - 1
                while(l < h): 
                    quad_sum = nums[i] + nums[j] + nums[l] + nums[h] 
                    if (quad_sum == target): 
                        res.append([nums[i], nums[j], nums[l], nums[h]]) 
                        l += 1
                        h -= 1
                        while(l < h and nums[l] == nums[l - 1]): l += 1
                        while(l < h and nums[h] == nums[h + 1]): h -= 1
                    elif(quad_sum < target): l += 1
                    else: h -= 1
        
        return res