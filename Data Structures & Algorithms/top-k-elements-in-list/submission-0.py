class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {} 
        for num in nums: 
            freq_map[num] = 1 + freq_map.get(num, 0)
        eleMap = []
        for key, v in freq_map.items(): 
            eleMap.append([v, key])
        eleMap.sort()
        res = []
        while(len(res) < k): 
            res.append(eleMap.pop()[1])
        return res
        