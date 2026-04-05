class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        h = {}  # Dictionary to track occurrences
        for num in nums:
            if num in h:
                return True  # Found a duplicate
            h[num] = 1  # Mark as seen
        return False  # No duplicates found

# Create an instance of the Solution class
solution = Solution()
