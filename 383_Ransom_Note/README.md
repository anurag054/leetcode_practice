# Ramsom Note
## Question:
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.  
Each letter in `magazine` can only be used once in `ransomNote`.  

`Example 1`:  
Input: ransomNote = "a", magazine = "b"  
Output: false

`Example 2`:  
Input: ransomNote = "aa", magazine = "ab"  
Output: false

`Example 3`:  
Input: ransomNote = "aa", magazine = "aab"  
Output: true

## My Solutions:
## 1. Using counter directly
In this process, the `frequency` of each character in `ransomNote` and `magazine` is counted using `counter`. Then it checks if the `magazine` has at least as many of each character as `ransomNotes`.
```python
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char, freq in ransom_count.items():
            if magazine_count[char] < freq:
                return False
        return True
```
Time Complexity: `O(m+n)`

## 2. Using manual hashmaps
Here, first we build a `frequencey dictionary` for all characters in magazine. Then, iterate through `ransomNote` and check if each character exists in `magazine_count`. If character is `missing or used up`, return `False`. Otherwise `decrement` the `counter`.
```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for char in magazine:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1

        for char in ransomNote:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1

        return True
```
Time Complexity: `O(m+n)`
