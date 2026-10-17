class Solution: 
    def can_ship(self, weights, mid, days):  
        took_days = 1
        freight = 0
        for w in weights: 
            if (freight + w <= mid): 
                freight += w 
            else: 
                freight = w
                took_days += 1 # New day loading. 
        return took_days <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, h = max(weights), sum(weights)  
        while(l <= h): 
            mid = (l + h)//2; 
            if (self.can_ship(weights, mid, days)): 
                ans = mid 
                h = mid - 1
            else: l = mid + 1 
        return ans 
        