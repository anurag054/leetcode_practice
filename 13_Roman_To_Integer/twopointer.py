class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0
        n = len(s)
        roman  = {
            "I":1, 
            "V":5,
            "X":10, 
            "L":50,
            "C":100,
            "D":500,
            "M":1000 
        }
        for i in range(n-1):
            curr,nxt = roman[s[i]] , roman[s[i+1]]
            if curr < nxt:
                val -= curr
            else:
                val += curr
        val += roman[s[n-1]]
        return val
