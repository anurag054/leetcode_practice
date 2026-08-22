# Best Time To Buy and Sell Stock
## Question:
You are given an array `prices` where `prices[i]` is the price of a given stock on the ith day.  

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.  

Return the `maximum profit` you can achieve from this transaction. If you cannot achieve any profit, return `0`.  

 

Example 1:  
Input: prices = [7,1,5,3,6,4]  
Output: 5  
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.  
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.  

Example 2:  
Input: prices = [7,6,4,3,1]  
Output: 0  
Explanation: In this case, no transactions are done and the max profit = 0.  

## My Solutions:
## 1. Brute-Force approach
At first as always due to my beginner habits, I approached it through the `brute force method`, where I used `nested loops` to check every possible combination of buying and selling days. For `every pair`, I calculated the profit by subtracting the buying price from the selling price. It is a `straightforward method`, but we all know due to nested loops, the `time complexity` turns out to be `O(n^2)` which is not efficient for large datasets.
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
```
After running this code, it passed some test cases but failed on the large datasets. So the `time complexity` and `large datasets` are a big problem using this approach.

## 2. Single-Pass approach
This approach was much simpler than the previous one. This one also used `loop` but not the nested ones. Here, I initialized the `minimum price` as `buy` and assigned it the value at `index zero`, while setting `profit to 0`. And the following code:
```python
class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
```
Here, the program completes with a `time complexity: O(n)`

## 3. Two-Pointer Approach
After these, I went on to search for better solutions and found a method which made use of `pointers`. The code logic was `similiar` although it made use of pointers so I thought of trying it too and including my learning of it here. 
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1   # l = buy pointer, r = sell pointer
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r     # if found a cheaper price, shift buy pointer
            r += 1
        return maxP
```
Similarly, the program completes with a `time complexity: O(n)` too.
  
