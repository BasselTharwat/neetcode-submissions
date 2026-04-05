class Solution:
    def findMin(self, nums: List[int]) -> int:

        # If the middle element is greater than the rightmost element,
        # then the smallest element is in the right half

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
        
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid


        return nums[left] # or nums[right]... they converged    
        


        