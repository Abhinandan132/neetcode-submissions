class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Naive approach T.C O(nlog(n)), S.C(O(1))
        nums.sort() 
        missing = 1 # Smallest +ve num assumed to be missing. 
        for num in nums: 
            if (num > 0 and missing == num): # Number in the array. 
                missing += 1
        return missing
            
