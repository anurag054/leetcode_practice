# First Bad Version
## Question

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.  

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.  

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the `first bad version`. You should `minimize` the number of `calls to the API`.  

`Example 1`:  
Input: n = 5, bad = 4  
Output: 4  
Explanation:  
call isBadVersion(3) -> false  
call isBadVersion(5) -> true  
call isBadVersion(4) -> true  
Then 4 is the first bad version.  

`Example 2`:  
Input: n = 1, bad = 1 
Output: 13  

# My Solutions:
By the theme of the question, I thought it would be related to binary searching due to which we could try and find the bad version in O(log n) time. So, that would be the optimal solution but I've also included the brute force approach as well because why not haha.

# Brute Force Approach
```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
            for i in range(1, n+1):
                if isBadVersion(i): 
                    return i
```

## Binary Search
```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n   # versions are 1..n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid - 1   # shrink range
            else:
                left = mid + 1
        return left   # first bad version
```
