class Solution:
    def findMin(self, nums: list[int]) -> int:
        sorted_arr = sorted(nums)

        return sorted_arr[0]
