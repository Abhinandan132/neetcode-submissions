class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) 
        l, h = 0, n - 1
        while(l < h): 
            if (numbers[l] + numbers[h] == target): return [l + 1, h + 1] 
            elif (numbers[l] + numbers[h] < target): l += 1
            else: h -= 1