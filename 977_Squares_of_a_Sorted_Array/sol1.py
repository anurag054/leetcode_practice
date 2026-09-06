class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = [pow(i,2) for i in nums]      #creates a list of squares
        return sorted(squared)
