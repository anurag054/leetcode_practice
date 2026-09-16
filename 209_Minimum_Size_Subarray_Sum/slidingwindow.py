class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        output = 0
        left = 0
        minimum_len = float('inf')      

        for right in range(len(nums)):
            output += nums[right]

            while output >= target:
                minimum_len = min(minimum_len, right - left + 1)
                output -= nums[left]
                left += 1

        return 0 if minimum_len == float('inf') else minimum_len
