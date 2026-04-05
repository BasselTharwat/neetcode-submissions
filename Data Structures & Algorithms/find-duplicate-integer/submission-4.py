class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hasher = {}

        for i in range(len(nums)):
            if nums[i] in hasher:
                return nums[i]
            else:
                hasher[nums[i]] = 1
        

            
        return 0