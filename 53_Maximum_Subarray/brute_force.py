class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]   
        n = len(nums)
        for i in range(n):
            current_sum = 0
                for j in range(i, n):
                    current_sum += nums[j]
                    max_sum = max(max_sum, current_sum)
            return max_sum
