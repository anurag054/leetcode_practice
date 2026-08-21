# leetcode_practice
Here, I practice leetcode problems beginning from the start learning it step-wise-step as I go on learning

## Two Sum problem
(You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example :
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].)

## My solutions
## Brute force approach:
'''python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
        for j in range(i+1, len(nums):
          if nums[i] + nums[j] == target:
            return[i,j]
'''

This was the solution I came up first thinking simply about using the loops(nested). But the use of the loops in the program causes the code to be less feasible because the nested loops causes the time complexity to be O(n^2).

But the optimal solution can be obtained through the use of hashmaps (dictionaries).
## Optimal solution (Using hashmaps)
'''python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {} # creating a empty hashmap containing val: index

       for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i] 

        seen[n]= i
'''
Here, the use of hashmap makes it easier for the solution to be found. 
And the time complexity results to : O(n) along with space complexity: O(n) too because the creation of hashmap causes to create a memory which utilizes the memory of the system.
