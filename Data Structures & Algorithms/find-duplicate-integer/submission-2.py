class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hasher = {}

        for num in nums:
            if num in hasher:
                return num
            
            hasher[num] = 1
        

            
        return 0