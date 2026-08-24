# Product of Array except Self ( `medium`)
## Question:
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the `division operation`.

Example 1:  
Input: nums = [1,2,3,4]  
Output: [24,12,8,6]  

Example 2:  
Input: nums = [-1,1,0,-3,3]  
Output: [0,0,9,0,0]  


## My Solutions:
## 1. Using slicing (Brute-force)
Well, while looking at the problem and at the condition that we cannot use the `division operator`, the first thing that came to my mind was ignoring/separating the `i'th` element and performing normal `multiplication operator` among the `remaining elements` and returning the list as output. Well it worked correctly for the `test cases` but failed on the `large datasets`.
```python

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []     #creating an empty list to store the output
        for i in range(len(nums)):
            others = nums[:i] + nums[i+1:]     #performing slicing to get the elements before i'th and after i'th element respectively. 
            product = 1       #initializing the value for the actual result
            for val in others:
                product *= val
            result.append(product)     #adding the result back to the list `result`
        return result
```
Well till now we already know what the problem is with this:
Time complexity : `O(n^2)`
Fails for `large datasets`.

## 2. Prefix - Suffix solution
Well after `trial and error`, with help of other `solutions` and going it through, this was the best solution. From my `point of view`, it was like a `divide and conquer` approach. I'd summarize it as:
- `prefix products`: product of all elements to the left of `i`
- `suffix products`: product of elements to the right of `i`
- `result[i] : prefix[i] * suffix[i]`

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n     #making result list same as the length nums

        prefix = 1       #initiating prefix as 1 for first index
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1       #initiating suffix as 1 for last index
        for i in range(n-1, -1, -1):     #accessing upto the first element from the last element
            result[i] *= suffix
            suffix *= nums[i]

        return result
```
Time complexity: `O(n)`  
Space complexity: `O(n)`

At first, I found this solution a bit difficult, and after some `dry numerical runs` on `pen and paper` and the concept finally got into my mind.  
`(reference screenshots for future purposes)`

<img width="943" height="481" alt="image" src="https://github.com/user-attachments/assets/0cd2e589-f1ba-424d-b840-36a5234873ac" /> 
  
<img width="915" height="478" alt="image" src="https://github.com/user-attachments/assets/e8d181cd-28e4-4495-a464-b37b1dfbc283" />


