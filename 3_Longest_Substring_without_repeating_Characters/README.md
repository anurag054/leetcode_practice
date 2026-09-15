# LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS   `MEDIUM`
## QUESTION:
Given a string `s`, find the length of the `longest` substring without `duplicate` characters.

`Example 1`:
Input: s = "abcabcbb"  
Output: 3  
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.  

`Example 2`:  
Input: s = "bbbbb"  
Output: 1  
Explanation: The answer is "b", with the length of 1.

`Example 3`:  
Input: s = "pwwkew"  
Output: 3  
Explanation: The answer is "wke", with the length of 3.  
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.  

## MY SOLUTIONS:
The problem is related to a `sliding window` problem where we make use of two pointers. Here, I declared the two pointers to be `left` and `right` and initialized the `max_len` to calculate the maximum length of the substring. Then I initialized a `set` so that no duplicate characters are included.
Then if the `value` pointed by the `right pointer` is found to be in the set then it is `removed` and again the process is carried on and if they are not `present`, they are `added` to the set. After that finally the `maximum length` is compared and returned.
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0 
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
```
Here, the time complexity of the problem is `O(n)`, and not `O(n^2)` because for every `while` it does not have to go to the `for` loop. Instead the problem advances `left` across the string. So the complexity is `linear`.  
Space Complexity: `O(n)`
