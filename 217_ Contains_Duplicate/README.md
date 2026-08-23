# Contains Duplicate
## Question:
Given an integer array `nums`, return `true` if any value appears `at least twice` in the array, and return `false` if every element is distinct.

 

`Example 1:`  
Input: nums = [1,2,3,1]  
Output: true  
Explanation: The element 1 occurs at the indices 0 and 3.  

`Example 2:`  
Input: nums = [1,2,3,4]  
Output: false  
Explanation: All elements are distinct.  

`Example 3:`  
Input: nums = [1,1,1,3,3,4,3,2,4,2]  
Output: true  

## My Solutions:

## 1. Brute Force approach
As always, let's go for the `brute force approach` first. Here, we loop through the entire array and then use `nested loop` to compare the values if they are found to be similar or not. Till now, we've already known this approach isn't very good approach for solving this, but being the `human nature` to try the brute force nature never goes. HAHA!!
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #going through brute force approach
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] == nums [j]:
                    return True
        return False
```
Time complexity : `O(n^2)`  
Space complexity: `O(1)`  
Also failed for `large datasets`  

## 2. Using the .sort() function 
`.sort()` function is a reliable function in python because it sorts the elements in the array without making use of complex `sorting algorithms`. In this approach, we first sort the elements in the array using the `.sort() function`. And then we compare the `adjacent values` in the array to find if there are `duplicate values` or not.
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #using .sort function
        nums.sort()
        for i in range (len(nums)-1):       #because the last index may go out of bounds if `minus one` is not done
            if nums [i] == nums [i+1]:
                return True
        return False
```
Time complexity : `O(n logn)`  
Space complexity: `O(n)` (In this case, `not totally "n"` but may lead to it at the `worst condition`)  
This method worked brilliantly in leetcode, but there is a another method where the time complexity can be reduced to `O(n)` using the `hashsets` in the hashing method.

## 3. Using Hashset
Using the `hashset`, we can easily find if there are any `duplicates` or not. The `sets` while taking in the value always tends to `check` whether it already contains the `same element` or not, and `discards` if it is the same element.
```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #using hashsets
        hashset = set()      #creating hashset using the set() function
        for i in nums:       #directly accessing the values rather than the index(where we use range)
            if i in hashset:
                return True
            hashset.add(i)    #adding to hashset if the value is'nt there

        return False    
```
Using this method, we `reduce` our `time complexity` but sacrifice our `memory utility`.  
Time complexity : `O(n)`    
Space complexity: `O(n)`  
