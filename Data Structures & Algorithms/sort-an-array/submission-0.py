class Solution:
    # Traditional merge sort relying on two helper functions. 
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums: List[int], low: int, mid: int, high: int) -> None: 
            temp, left, right = [], low, mid + 1# Assign pointers. 
            while(left <= mid and right <= high): 
                if (nums[left] <= nums[right]): 
                    temp.append(nums[left])
                    left += 1
                else: 
                    temp.append(nums[right])  
                    right += 1
            # Existing elements are copied if any. 
            while(left <= mid): 
                temp.append(nums[left]) 
                left += 1
            while(right <= high): 
                temp.append(nums[right]) 
                right += 1
            for i in range(low, high + 1): 
                nums[i] = temp[i - low] 

        def mergeSort(nums: List[int], low: int, high: int) -> None: 
            if (low >= high): 
                return 
            mid = (low + high) // 2
            # Merge sort on the left half. 
            mergeSort(nums, low, mid) 
            # Merge sort on the right half
            mergeSort(nums, mid + 1, high) 
            # Merge the sorted arrays.
            merge(nums, low, mid, high)

        mergeSort(nums, 0, len(nums) - 1)
        return nums