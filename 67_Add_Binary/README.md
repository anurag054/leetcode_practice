# ADD BINARY
## QUESTION:
Given two binary strings `a` and `b`, return their sum as a binary string.

`Example 1`:  
Input: a = "11", b = "1"  
Output: "100"  

`Example 2:`  
Input: a = "1010", b = "1011"  
Output: "10101"  

## MY SOLUTIONS:
## 1. Using built in function: 'bin'
Here, we can directly convert their sum into the binary by using the `bin` keyword.
```python
def addBinary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]
```
- `int(a, 2)` → converts binary string a into a decimal integer  
- `int(b, 2)` → converts binary string b into a decimal integer  
- Add them together  
- `bin(...)` → converts the sum back into a binary string (with a `0b` prefix)  
- `[2:]` → slices off the `0b` prefix, leaving just the binary digits


## 2. Algorithmic Approach
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        # Process both strings from right to left
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            # Append the current bit
            result.append(str(total % 2))
            # Update carry
            carry = total // 2

        # Reverse to get the correct order
        return "".join(reversed(result))
```
- Start from the last digit of both strings (like manual addition)  
- Add corresponding bits plus any carry  
- Store the result bit (`total % 2`) and update carry (`total // 2`)  
- Continue until all bits are processed  
- Reverse the result list to form the final binary string

