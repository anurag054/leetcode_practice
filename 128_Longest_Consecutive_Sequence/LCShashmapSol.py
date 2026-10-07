class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            # Only start if num is the beginning of a sequence
            if num - 1 not in nums:
                current = num
                count = 1

                while current + 1 in nums:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest
