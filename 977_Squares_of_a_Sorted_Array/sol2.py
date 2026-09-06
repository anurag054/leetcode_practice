class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            sq = num * num
            arr.append(sq)
        arr.sort()

        return arr
