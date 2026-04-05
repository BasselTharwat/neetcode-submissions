class Solution:
    """
    0, 0, 0
    l  i  r
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
            
        sorted_arr = sorted(nums)
        triplets_set = set()
        


        for i in range(1, len(nums)-1):
            left = i - 1
            right = i + 1
            while left > -1 and right < len(nums):
                value = sorted_arr[left] + sorted_arr[i] + sorted_arr[right]
                if value > 0:
                    left -= 1
                elif value < 0:
                    right += 1
                else:
                    triplet = (sorted_arr[left] , sorted_arr[i] , sorted_arr[right])
                    if triplet not in triplets_set:
                        triplets_set.add(triplet)
                    left -= 1
                    right += 1



        
        return [list(t) for t in triplets_set]
        