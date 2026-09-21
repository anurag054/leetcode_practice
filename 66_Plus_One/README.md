# PLUS ONE
## QUESTION:
You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `ith` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0's`.  
Increment the large integer by one and return the resulting array of digits.  

`Example 1`:  
Input: digits = [1,2,3]  
Output: [1,2,4]  
Explanation: The array represents the integer 123.  
Incrementing by one gives 123 + 1 = 124.  
Thus, the result should be [1,2,4].  

`Example 2`:  
Input: digits = [4,3,2,1]  
Output: [4,3,2,2]  
Explanation: The array represents the integer 4321.  
Incrementing by one gives 4321 + 1 = 4322.  
Thus, the result should be [4,3,2,2].  

`Example 3`:   
Input: digits = [9]  
Output: [1,0]  
Explanation: The array represents the integer 9.  
Incrementing by one gives 9 + 1 = 10.  
Thus, the result should be [1,0].  

## MY SOLUTIONS:
Here, the `last index` is accessed and then it is incremented by `one`. If there is `carry over`, the last digit is considered to be `0` and then the digit `before that digit` is incremented by `one` to show the carry over. And if all the numbers are `9`, then `1` is appended to the array and then displayed.
```python
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1         #starting from the last
        while i >= 0:       #traverse from the end
            digits[i] += 1      #adding 1 to the last digit

            if digits[i] < 10:      #no carry condition
                return digits       #return the same number as there is no carry

            digits[i] = 0       #if carry, the last number would be 0 
            i -= 1              # then the i shifts to previous digit and increment it through loop

        return [1] + digits         #for the array with all 9s, because they would be all 0s, which would lead us to add 1 to the beginning to make it valid. otherwise it would be all zeros
```
Time complexity: O(n)  
Space complexity: O(10  

There is a direct approach to this too. Here, we convert into integer, add it and return back to the string.
```python
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        num = int("".join(map(str, digits)))     # Convert list of digits to integer
        num += 1       # Add one
        return [int(d) for d in str(num)]      # Convert back to list of digits
```
This approach is short and simple but not `memory efficient` for `large data` inputs.
