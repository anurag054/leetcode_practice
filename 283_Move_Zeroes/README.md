# Move Zeroes
## Question:
Given an integer array `nums`, move all `0's` to the `end` of it while maintaining the `relative order` of the `non-zero` elements.  
Note that you must do this in-place without making a copy of the array.  

`Example 1`:  
Input: nums = [0,1,0,3,12]  
Output: [1,3,12,0,0]  

`Example 2`:  
Input: nums = [0]  
Output: [0]  

## My Solutions:
## 1. Swapping Approach
``` python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Pointer for the next position to place a non-zero
        last_non_zero = 0

        # Traverse the array
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap current non-zero with the element at last_non_zero
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1
```

## 2. Two Pointers:
```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Pointer for the position of the next non-zero element
        insert_pos = 0

        # Step 1: Move non-zero elements forward
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        # Step 2: Fill the rest with zeros
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
```
