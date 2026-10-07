# LONGEST CONSECUTIVE SEQUENCE (`MEDIUM`)
## QUESTION:
Given an unsorted array of integers `nums`, return the `length` of the `longest consecutive` elements sequence.  

You must write an algorithm that runs in `O(n)` time.  

`Example 1`:  
Input: nums = [100,4,200,1,3,2]  
Output: 4  
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.  

`Example 2`:  
Input: nums = [0,3,7,2,5,8,4,6,0,1]  
Output: 9  

`Example 3`:  
Input: nums = [1,0,1,2]   
Output: 3  

 ## MY SOLUTIONS:
 The approach behind this is to use a `hashmaps`. We could also do it by `sorting` but by the definitions of the question, we are to solve within `O(n)` time complexity, so we make use of only hashmaps without use of sort function.  
 So, the concept behind the solution is: 
 - declaring a `hashset` and the `longest` variable
 - iterating over the declared `hashset`
 - `expanding` the sequence forward
 - updating the `longest` length

```python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)     #hashset declaration
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
```
