# THREE SUM
## QUESTION:
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0.`  

Notice that the solution set must not contain `duplicate triplets`.    

`Example 1`:  
Input: nums = [-1,0,1,2,-1,-4]  
Output: [[-1,-1,2],[-1,0,1]]  
Explanation:   
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.  
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.  
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.  
The distinct triplets are [-1,0,1] and [-1,-1,2].  
Notice that the order of the output and the order of the triplets does not matter.  

`Example 2`:  
Input: nums = [0,1,1]  
Output: []  
Explanation: The only possible triplet does not sum up to 0.  

`Example 3`:  
Input: nums = [0,0,0]  
Output: [[0,0,0]]  
Explanation: The only possible triplet sums up to 0.  

# SOLUTION:
We could apply brute force approach to this solution but that way the time complexity would be `O(n^3)`.  
So, we use the `pointer approach` instead.
```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()     #sorting the nums since we have to use pointers to find the exact triplets.

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:     #checking if same values of i occur as before
                continue

            j = i + 1     #points to the second value after i
            k = len(nums) - 1     #start from the last of the list

            while j < k:     # j must always be less than k
                threeSum = nums[i] + nums[j] + nums[k]

                if threeSum > 0:
                    k -= 1     # in sorted list, if sum results greater than 0, then the value must be decreased so decrementing the higher value
                elif threeSum < 0:
                    j += 1     # same as above but if negative, then we've to increase the value
                else:
                    result.append([nums[i], nums[j], nums[k]])     # triplet found, so appending it to the result
                    j += 1     # after finding one triplet, searching for another triplets for the same condition for same `i`

                    while nums[j] == nums[j - 1] and j < k:     # checking if same value of j is present at another index
                        j += 1
            
        return result
```
Time Complexity: `O(n ^ 2)`  
Space Complexity: `O(n)`
