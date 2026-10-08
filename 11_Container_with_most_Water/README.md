# CONTAINER WITH MOST WATER
## QUESTION:
You are given an integer rray `height` of length `n`. There are n vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the `x-axis` form a container, such that the container contains the `most water`.

Return the `maximum` amount of water a container can store.

Notice that you may not `slant` the container.

 

`Example 1`:  
<img width="801" height="383" alt="image" src="https://github.com/user-attachments/assets/cf04449f-e7be-49a7-9080-314a29b05002" />

Input: height = [1,8,6,2,5,4,8,3,7]  
Output: 49  
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.  

`Example 2`:  
Input: height = [1,1]  
Output: 1  

## MY SOLUTIONS:
The best way to approach this solution is to make use of `two pointers`. This creates an rather optimal approach without making using for `nested loops` or `sorting`.  
The main idea behind the solution is:
- initialize `left` and `right` pointers to `0` and `len(height) - 1`
- compute the area with the formula: `area = min(height[left], height[right]) * (right - left)`
- update the `max_area` if the area is larger
- move the pointers inward since the shorter one limits the area
- repeat until `left` and `right` meets
- return `max_area`

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0 

        while left < right:
            current_area = min(height[left], height[right]) * (right - left)        #the maximum area it can cover is the minimum height multplied by it's width
            max_area = max(current_area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```
