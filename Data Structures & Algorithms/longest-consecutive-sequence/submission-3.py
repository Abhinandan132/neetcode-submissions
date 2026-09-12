class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Naive approach, sort and return the longest length. 
        if (len(nums) == 0): return 0
        nums.sort() 
        max_length, curr_length = 1, 1 
        for i in range(1, len(nums)): 
            if (nums[i] - nums[i - 1] == 1): 
                curr_length += 1
                max_length = max(max_length, curr_length)
            elif (nums[i] == nums[i - 1]): 
                continue
            else:  
                curr_length = 1
        return max_length