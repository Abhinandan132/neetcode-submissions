from math import ceil 
class Solution: 
    def can_eat(self, piles, mid, h):  
        total_hours = 0
        for b in piles: 
            total_hours += ceil(b/mid) 
        return total_hours <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = -1
        while(left <= right): 
            mid = (left + right)//2; 
            if (self.can_eat(piles, mid, h)): 
                ans = mid
                right = mid - 1
            else: left = mid + 1
        return ans 
    
        