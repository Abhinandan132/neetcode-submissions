class Solution:
    def trap(self, height: List[int]) -> int:
        # Naive approach. T.C O(n^2), compute lmax, rmax for every index. 
        n = len(height) 
        if (n == 0): return 0
        # res = 0
        # for i in range(n): 
        #     left_max = right_max = height[i] 
        #     for j in range(i): 
        #         left_max = max(left_max, height[j]) 
        #     for j in range(i + 1, n): 
        #         right_max = max(right_max, height[j]) 
        #     res += min(left_max, right_max) - height[i] 
        # return res
        left_max = [0] * n
        right_max = [0] * n 
        left_max[0] = height[0] 
        for i in range(1, n): 
            left_max[i] = max(left_max[i - 1], height[i]) 
        right_max[n - 1] = height[n - 1] 
        res = 0
        for i in range(n - 2, -1, -1): 
            right_max[i] = max(right_max[i + 1], height[i]) 
        for i  in range(n): 
            res += min(left_max[i], right_max[i]) - height[i] 
        return res
