class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = []
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                squared.append(nums[l] * nums[l])
                l += 1
            else:
                squared.append(nums[r] * nums[r])
                r -= 1

        return squared[::-1]  
