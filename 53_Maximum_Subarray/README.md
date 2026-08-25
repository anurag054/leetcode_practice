# Maximum Subarray (`medium`)
## Question:
Given an integer array `nums`, find the `subarray` with the `largest sum`, and return its sum.

`Example 1:`  
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]  
Output: 6  
Explanation: The subarray [4,-1,2,1] has the largest sum 6.  

`Example 2:`  
Input: nums = [1]  
Output: 1  
Explanation: The subarray [1] has the largest sum 1.  

`Example 3:`  
Input: nums = [5,4,-1,7,8]  
Output: 23  
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.  

## My solutions:
## 1. Brute-Force method
The method was to initialize the `max_sum` to the first element and shifting it's value if greater sum is found using the another variable `current_sum`. Although `inefficient`, it gets the work done for `smaller datasets`.
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]   # starting with first element
        n = len(nums)
        for i in range(n):
            current_sum = 0
                for j in range(i, n):
                    current_sum += nums[j]
                    max_sum = max(max_sum, current_sum)
            return max_sum
```
Time complexity: O(n^2)

## 2. Kadane's Algorithm
Kadane’s Algorithm is a dynamic programming technique used to find the maximum subarray sum in linear time.

### Intuition
At each index, you decide:
- **Extend the previous subarray** (add current element to the running sum), or
- **Start a new subarray** beginning at the current element.

This choice ensures you always keep track of the best possible sum ending at each position.

### Algorithm Steps
1. Initialize:
   - `current_sum = nums[0]` → max sum ending at the first element
   - `max_sum = nums[0]` → global maximum so far
2. For each element `nums[i]` (from index 1 onward):
   - Update running sum:  
     `current_sum = max(nums[i], current_sum + nums[i])`
   - Update global max:  
     `max_sum = max(max_sum, current_sum)`
3. Return `max_sum`.

   ```python
   class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currentSum = 0

        for i in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += i
            maxSub = max(maxSub, currentSum)
        return maxSub
   ```
### Cleaner version (for learning)
```python
def max_subarray_kadane(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum
```
Time Complexity: O(n)  

There were other approaches too including the `recursive`, `dp-tabulation`, `dp-memoization` and others method too but the best one here is `Kadane's Algorithm`, so I decided to stick to this approach rather than using all other appoaches.
