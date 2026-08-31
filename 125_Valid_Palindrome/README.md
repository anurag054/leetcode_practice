# Valid Palindrome
## Question:
A phrase is a `palindrome` if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same `forward` and `backward`. `Alphanumeric` characters include `letters` and `numbers`.

Given a string `s`, return `true` if it is a `palindrome`, or `false` otherwise.

`Example 1`:  
Input: s = "A man, a plan, a canal: Panama"  
Output: true  
Explanation: "amanaplanacanalpanama" is a palindrome.

`Example 2`:  
Input: s = "race a car"  
Output: false  
Explanation: "raceacar" is not a palindrome.

`Example 3`:  
Input: s = " "  
Output: true  
Explanation: s is an empty string "" after removing non-alphanumeric characters.  
Since an empty string reads the same forward and backward, it is a palindrome.

## My Solutions:
## 1. Slicing Approach
In this approach, we directly slice the string for it's reversal and check for validity. Here, string cleaning is done by "".join() function.
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        return s == s[::-1]     #checking for reverse
```
- `.isalnum()` returns `True` if the character is a letter (`a–z`, `A–Z`) or a digit (`0–9`).  
  (Spaces, commas, punctuation, etc. are skipped.)
- `ch.lower()` ensures all cases letters are treated the same (both are considered as lowercase)
- `"".join()` takes all the filtered, lowercased characters and stitches them together into one new string.

## Two Pointer Technique
This method is considered more efficient because it does not require `extra memory space` but the time complexity remains the same i.e. `O(n)`.
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # Skip non-alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare ignoring case
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True
```
