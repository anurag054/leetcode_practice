# SQUARES OF A SORTED ARRAY
## QUESTION:
Given an integer array `nums` sorted in non-decreasing order, return an array of the `squares` of each number sorted in `non-decreasing order`.  

`Example 1`:  
Input: nums = [-4,-1,0,3,10]  
Output: [0,1,9,16,100]  
Explanation: After squaring, the array becomes [16,1,0,9,100].  
After sorting, it becomes [0,1,9,16,100].    

`Example 2`:  
Input: nums = [-7,-3,2,3,11]  
Output: [4,9,9,49,121]  

## My Solutions:
Basic approach is to raise the numbers to the power of two by traversing all the elements in the array.
```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = [pow(i,2) for i in nums]      #creates a list of squares
        return sorted(squared)
```

Same process but another way to do this is singly square the numbers and append it to the list.
```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            sq = num * num
            arr.append(sq)
        arr.sort()

        return arr
```
But these both solutions use the sort() function, so the time complexity comes out to be O(n logn) due to sorting.
The better approach is to make use of two pointers and compare their values accordingly.
```python
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

        return squared[::-1]  # reverse to get sorted order
```
Here, instead of comparing `squares of nums`, we could compare the  `absolute values` of `nums` because squaring takes `more time` than that of absolute.
Here, the `time complexity` results to be `O(n)`.
