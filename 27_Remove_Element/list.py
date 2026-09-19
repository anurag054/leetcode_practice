class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = []
        for i in range(len(nums)):
            if nums[i] != val:
                k.append(nums[i])
        nums[:] = k
        return len(k)
