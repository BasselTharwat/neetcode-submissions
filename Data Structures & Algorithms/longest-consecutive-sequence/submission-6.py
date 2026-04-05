class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums = sorted(nums)
        print(nums)

        longest = 0

        current_count = 1
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i] + 1:                
                current_count += 1
                print(current_count)
            elif nums[i+1] == nums[i]:
                pass
            else:
                if current_count >= longest:
                    longest = current_count
                current_count = 1
                print("out")
            
        if current_count >= longest:
                longest = current_count

        return longest


        