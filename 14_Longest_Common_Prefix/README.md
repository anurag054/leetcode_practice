# Longest Common Prefix
## Question:
Write a function to find the `longest common prefix` string amongst an array of strings.  
If there is no common prefix, return an `empty string ""`.  

`Example 1`:  
Input: strs = ["flower","flow","flight"]  
Output: "fl"  

`Example 2`:  
Input: strs = ["dog","racecar","car"]  
Output: ""  
Explanation: There is no common prefix among the input strings.  

## My Solution:
The concept behind the solution was to initiate the `first element` in the array as `prefix`. Then, we `loop` to the whole array starting from the `first index`. Now we compare the `string` with the `prefix` if it starts with the prefix or not, if `yes` then it returns the `prefix`, else it `cuts off` the `last character` until the match is `found` or nothing is `left` to compare.
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]     #initializing the first string as prefix
        for s in strs[1 : ]: 
            while not s.startswith(prefix):     #checking if other elements starts with the first string or not
                prefix = prefix[: -1]       #if not matched, the last char of the prefix is cut off
                if not prefix:       #nothing left condition
                    return ""
        
        return prefix
```

Time Complexity: `O(N.M)` where `N = number of strings` & `M = length of shortest string`  
Space Complexity: `O(1)`, since only `prefix` is stored
