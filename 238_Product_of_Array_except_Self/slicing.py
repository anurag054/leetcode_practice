
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []      
        for i in range(len(nums)):
            others = nums[:i] + nums[i+1:]      
            product = 1        
            for val in others:
                product *= val
            result.append(product)     
        return result
