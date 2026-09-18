# VALID PARENTHESES
## QUESTION:
Given a string `s` containing just the characters `'(', ')', '{', '}', '[' and ']'`, determine if the input string is valid.  

An input string is valid if:  

Open brackets must be closed by the same type of brackets.  
Open brackets must be closed in the correct order.  
Every close bracket has a corresponding open bracket of the same type.  
  
`Example 1`:  
Input: s = "()"  
Output: true  

`Example 2`:  
Input: s = "()[]{}"  
Output: true  

`Example 3`:  
Input: s = "(]"  
Output: false  

`Example 4`:  
Input: s = "([])"  
Output: true  

`Example 5`:  
Input: s = "([)]"  
Output: false  

## MY SOLUTIONS:
## USING A HASMAP ( MAPPING )
Here, we try to `map` each `closing` brackets to their respective `opening` brackets. While we store the `opening` brackets in a `stack`, we `pop` them as their respective brackets come in their respective `order`.
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif i in mapping:
                if not stack or stack[-1] != mapping[i]:
                    return False
                else:
                    stack.pop()

        return not stack
```
Time Complexity: `O(n)`  
Space Complexity: `O(n)`  

There is another simple approach for the solution as well but the above one is the best as it maps the respective values and is more flexible to use. But, I am also attaching another process as well.
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if stack and ((i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{')):
                stack.pop()
            else:
                stack.append(i)
        
        
        return not stack
```
