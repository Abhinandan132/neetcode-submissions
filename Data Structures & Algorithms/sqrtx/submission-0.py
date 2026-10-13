class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 1, x
        while(l <= h): 
            mid = (l + h)//2; 
            if (mid * mid <= x): l = mid + 1; 
            else: h = mid - 1
        return h