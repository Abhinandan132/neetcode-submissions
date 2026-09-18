class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() 
        l, h, cnt = 0, len(people) - 1, 0 
        while(l <= h): 
            if (people[l] + people[h] <= limit): 
                cnt += 1
                l += 1
                h -= 1
            # Case where limit exceeds
            elif (people[h] <= limit):  
                cnt += 1
                h -= 1
            else: 
                cnt += 1
                l += 1
        return cnt
        
