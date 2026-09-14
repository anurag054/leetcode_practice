# Climbing Stairs
## Question:
You are climbing a staircase. It takes `n` steps to reach the `top`.  
Each time you can either climb `1` or `2` steps. In how many `distinct ways` can you climb to the top?  

`Example 1`:  
Input: n = 2  
Output: 2  
Explanation: There are two ways to climb to the top.  
1. 1 step + 1 step  
2. 2 steps  
   
`Example 2`:  
Input: n = 3  
Output: 3  
Explanation: There are three ways to climb to the top.  
1. 1 step + 1 step + 1 step  
2. 1 step + 2 steps  
3. 2 steps + 1 step

## My Solutions:
The approach to solve this problem was to simply implement a `fibonacci` series. Or so I had thought...
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
```
This approach worked for some cases but not viable for all and the `time complexity` turns out to be `O(2^n)`. There would be `redundant calculations` and no `memoization` is involved.

This problem can be approached with a proper `dynamic programming` approach where the time complexity is reduced to `O(n)` and space complexity to `O(1)`
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n

        a, b = 1, 2
        for i in range( 3, n+1):
            a, b = b, a+b
        return b
```
