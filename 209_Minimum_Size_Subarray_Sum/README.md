# MINIMUM SIZE SUBARRAY SUM     `MEDIUM`
## QUESTION:  
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a `subarray` whose sum is greater than or equal to `target`. If there is no such subarray, return` 0 `instead.  

`Example 1`:  
Input: target = 7, nums = [2,3,1,2,4,3]  
Output: 2  
Explanation: The subarray [4,3] has the minimal length under the problem constraint.  

`Example 2`:  
Input: target = 4, nums = [1,4,4]  
Output: 1  

`Example 3`:  
Input: target = 11, nums = [1,1,1,1,1,1,1,1]  
Output: 0  

## MY SOLUTIONS:
This solution can also be approached using a nested loop but the time complexity turns out to be `O(n^2)`.   
So instead of that, we discard that method and we directly use the `sliding window` approach which gives us the `time complexity` to the solution `O(n)`.
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        output = 0
        left = 0
        minimum_len = float('inf')      #starting with positive infinity, the first valid subarray length would replace it

        for right in range(len(nums)):
            output += nums[right]

            while output >= target:
                minimum_len = min(minimum_len, right - left + 1)
                output -= nums[left]
                left += 1

        return 0 if minimum_len == float('inf') else minimum_len
```
