# Group Anagrams (`medium`)
## Question:
Given an array of `strings` strs, group the `anagrams` together. You can return the answer in any order.

`Example 1`:  
Input: strs = ["eat","tea","tan","ate","nat","bat"]  
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]  

Explanation:  
There is no string in strs that can be rearranged to form "bat".  
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.  
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.  

`Example 2`:  
Input: strs = [""]  
Output: [[""]]  

`Example 3`:  
Input: strs = ["a"]  
Output: [["a"]]  

## My Solutions:
## Using .sorted function
Here, we can use `.sorted()` function in the given array of strings and create a `key` for storing in `dictionary` and find their `anagrams` as according to their respective `keys`.
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for word in strs:
            key ="".join(sorted(word))
            if key not in output:
                output[key] = []
            output[key].append(word)
        
        return list(output.values())
```
