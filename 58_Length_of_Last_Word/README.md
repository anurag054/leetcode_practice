# LENGTH OF LAST WORD
## QUESTION:
Given a string `s` consisting of `words` and `spaces`, return the `length` of the `last word` in the string.  
A word is a maximal substring consisting of non-space characters only.  

`Example 1`:  
Input: s = "Hello World"  
Output: 5  
Explanation: The last word is "World" with length 5.  

`Example 2`:  
Input: s = "   fly me   to   the moon  "  
Output: 4  
Explanation: The last word is "moon" with length 4.  

`Example 3`:  
Input: s = "luffy is still joyboy"  
Output: 6  
Explanation: The last word is "joyboy" with length 6.  

## MY SOLUTIONS:
## 1. Using .strip() and .split()
This is a classic string problem in python. We could directly use the `.split()` to `split the words to individual elements` and `.strip()` to `remove the leading and trailing spaces` and directly return the `length` of the last word.
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1]) if words else 0
```
## 2. Without using the in-built function
In this approach, we `strip` the spaces `manually` and then access the last word of the string. Here, the `space complexity` would be reduced to `O(1)`.
```
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0     # starting at the last index

        while s[i] == " ":     #stripping off the trailing spaces
            i -= 1     #getting to the last character if there is space

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
```
