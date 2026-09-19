# REMOVE ELEMENT
## QUESTION:
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.  

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:  

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.  

Custom Judge:  
The judge will test your solution with the following code:  
```
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be accepted.  

`Example 1`:  
Input: nums = [3,2,2,3], val = 3  
Output: 2, nums = [2,2,_,_]  
Explanation: Your function should return k = 2, with the first two elements of nums being 2.  
It does not matter what you leave beyond the returned k (hence they are underscores).    

`Example 2`:  
Input: nums = [0,1,2,2,3,0,4,2], val = 2  
Output: 5, nums = [0,1,4,0,3,_,_,_]  
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.  
Note that the five elements can be returned in any order.  
It does not matter what you leave beyond the returned k (hence they are underscores).  

## My Solutions:
Here, we iterate through the list and then compare the values and if the `value` is not present in the list, then we `append` it to the index of `k` which was initialized to `0` at first and `increment` the value of `k`.
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0            # k keeps track of the index where the next valid element should go

        for i in range(len(nums)):
            if nums[i] != val:        # If the current element is not the target value
                nums[k] = nums[i]       # Place it at the index k and increment k
                k += 1
                
        return k       # k represents the total number of elements not equal to val
```
Time Complexity : `O(n)`  
Space Complexity : `O(1)`  

There is another easy way to solve this problem as well but an extra list would be created which would lead the `space complexity` to be `O(n)`. So, the upper one is more preferable. But for the context only, I am including that block of code as well.
```python
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = []
        for i in range(len(nums)):
            if nums[i] != val:
                k.append(nums[i])
        nums[:] = k
        return len(k)
```
