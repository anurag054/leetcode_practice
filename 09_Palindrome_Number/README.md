# Palindrome Number

## Question:
Given an integer `x`, return true if `x` is a palindrome, and false otherwise.  

### Examples

**Example 1:**  
Input: `x = 121`  
Output: `true`  
Explanation: 121 reads as 121 from left to right and from right to left.  

**Example 2:**  
Input: `x = -121`  
Output: `false`  
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.  

**Example 3:**  
Input: `x = 10`  
Output: `false`  
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

## My Solutions
My first approach for solving this problem was to use the `reverse string method` which is a very commonly used method of string. Since we can `explicitly` change the given number into strings and perceive it as string, we could apply the same method as in the string to get the reverse of the number too. This approach is a bit easier in python, so that's the first approach that came into my mind while solving this problem.
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
```
Here, I compared the previously given number to the number after `reversing(through slicing)` and returned the boolean value whether it'll be true or false.
This method was simple and effective but used `extra memory`. Time complexity: `O(n)`

Now on another thought, I thought that the methods we used to do in other `PL like C`, in which we reversed the numbers mathematically, `digit by digit`, and compare it to the original number would present to be more effective since it `avoids the string conversion` as well as use `constant space` rather than taking extra memory for conversion.
``` python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reverse = 0

        while x != 0:
            digit = x % 10    #modular division to get the last digit
            reverse = reverse * 10 + digit     #getting the last digit in reverse order and eventually all the digits
            x //= 10     #chopping out the last digit

        return original == reverse
```
Here, the time complexity turns out to be `O(logn)` and & space complexity to be `O(1)` since only a few variables are used.

Comparatively, I found the previous method comparatively easy as it didn't include the calculations. But after going through some `numeric examples` I was able to understand the method behind this, and was able to construct the above program.

<img width="876" height="240" alt="image" src="https://github.com/user-attachments/assets/d870cc01-12ed-4d63-921b-20d1177784f8" />
