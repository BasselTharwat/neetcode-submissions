class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0 for i in range(len(nums))]
        zeroFound = False
        zeroFoundIndex = 0
        prod = 1
        
        # find zeros. one zero = result has one value only. multiple zeros = result is all zeros
        for i in range(len(nums)):
            if nums[i] == 0 and zeroFound == True:
                return result
            elif nums[i] == 0:
                zeroFound = True
                zeroFoundIndex = i
            else:
                prod *= nums[i]

        # fill in results array
        for j in range(len(nums)):
            if zeroFound == True and j == zeroFoundIndex:
                result[j] = prod
            elif zeroFound == False:
                result[j] = prod // nums[j]
            
        return result

            
                
            



        