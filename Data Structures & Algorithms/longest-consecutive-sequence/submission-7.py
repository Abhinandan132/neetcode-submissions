class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Naive approach, sort and return the longest length. 
        if (not nums): return 0
        # nums.sort() 
        max_length = 0
        # for i in range(1, len(nums)): 
        #     if (nums[i] - nums[i - 1] == 1): 
        #         curr_length += 1
        #         max_length = max(max_length, curr_length)
        #     elif (nums[i] == nums[i - 1]): 
        #         continue
        #     else:  
        #         curr_length = 1
        # return max_length
        # Optimal Approach: Hash T.C O(n), S.C: O(n) 
        num_map  = set(nums)
        for num in num_map: 
            if (num - 1 not in num_map): # The start of a subsequence? 
                curr_num = num 
                curr_len = 1
                while(curr_num + 1 in num_map): # Is a subsequence. 
                    curr_len += 1
                    curr_num += 1
                max_length = max(max_length, curr_len)
        return max_length

        
        