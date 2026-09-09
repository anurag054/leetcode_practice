# Remove Duplicates from Sorted Array
## Question:

Given an integer array `nums` sorted in `non-decreasing order`, remove the duplicates `in-place` such that each unique element appears only `once`. The `relative order` of the elements should be kept the `same`.  
Consider the number of `unique elements` in nums to be `k`​​​​​​​​​​​​​​. After removing `duplicates`, return the number of unique elements `k`.  
The first `k` elements of `nums` should contain the unique numbers in `sorted` order. The remaining elements beyond index `k - 1` can be ignored.  

`Custom Judge:`

The judge will test your solution with the following code:
```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be accepted.  

`Example 1`:  
Input: nums = [1,1,2]  
Output: 2, nums = [1,2,_]  
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.  
It does not matter what you leave beyond the returned k (hence they are underscores).  

`Example 2`:  
Input: nums = [0,0,1,1,1,2,2,3,3,4]  
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]  
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.  
It does not matter what you leave beyond the returned k (hence they are underscores).    

## My Solutions:
At first my `naive` approach was to solve it by making it a `set` and returning it. But the approach required `extra memory` to set up and making a set doesn't guarantee to `preserve it's order`. So the best method was to use a `two pointer approach` which is done below.

## Two Pointer Approach
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:     #checking for empty inputs     
            return 0

        i = 0     #slow pointer which marks the position of the last unique element found
        for j in range(1, len(nums)):
            if nums[j]!= nums[i]:
                i += 1
                nums[i] = nums[j]       #overwrite the slot with the unique value
        return i+1
```
