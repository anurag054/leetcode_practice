# Search Insert Position
## Question

Given a sorted array of distinct integers and a `target` value, return the `index` if the `target` is found. If not, return the `index` where it would be if it were `inserted in order`.  

You must write an algorithm with `O(log n)` runtime complexity.  
  
`Example 1`:  
Input: nums = [1,3,5,6], target = 5  
Output: 2  

`Example 2`:  
Input: nums = [1,3,5,6], target = 2  
Output: 1  

`Example 3`:  
Input: nums = [1,3,5,6], target = 7  
Output: 4  

## My Solutions:
The simple approach to this problem is to perform a binary search which will give us the `O(log n)` time complexity.
As for to return the required index, it would be stored in the left pointer. I figured it out when I did a dry run with the help of an example.

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1 
        
        while l<=r:
            mid = (l+r)// 2
            
            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                r -= 1
            
            else:
                l += 1

        return l        #here the final value at which the index stops is the index where the target would be found or the required index for the number to be inserted
```
