# Valid Anagram
## Question:
Given two strings `s` and `t`, return `true` if `t` is an `anagram` of `s`, and `false` otherwise.  

`Example 1`:  
Input: s = "anagram", t = "nagaram"  
Output: true  

`Example 2`:  
Input: s = "rat", t = "car"  
Output: false

## My solutions:
# Using sorted()
By directly using the sorted() function, we can directly check whether they are anagrams or not. This works by sorting out the characters of strings in sorted order on the basis of unicode code point order( or simply alphabetical order).
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```
Since, `sorting` is used in this process, the time complexity results to `O(n logn)`.

## Using hashmaps
Using `hashamaps`, the `extra step` of sorting can be `reduced` and hence code can be further optimized.
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):     #base condition
            return False

        countS, countT = {}, {}     #initializing empty dictionaries to store character count

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1     #if character isn't in the dictionary yet, start at 0. Then add one to the count
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT
```
Time complexity: `O(n)`

## Using counters
`Counter` is a special class from Python's collection module which works like a `dictionary`, but it's designed specifically to count how many times `each element appears`. 

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```
 The way the `counter` works is it tabulates the number of times a characters appear in the `stirng(list, tuple,etc)`.
 ```
s = "anagram"
t = "nagaram"

Counter(s) → {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
Counter(t) → {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}
```
Time complexity: `O(n)`



