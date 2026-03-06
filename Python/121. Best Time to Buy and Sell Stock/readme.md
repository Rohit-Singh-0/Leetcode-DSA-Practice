[121\. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
=======================================================================================================

📝 Problem Description
----------------------

You are given an array prices where prices\[i\] is the price of a given stock on the $i^{th}$ day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

💡 Thought Process
------------------

### 1\. Brute Force Approach

The naive way is to calculate the profit for every possible pair of buy and sell days.

*   **Logic:** Use nested loops. The outer loop represents the buy day, and the inner loop represents the sell day (must be after the buy day).
    
*   **Update:** max\_profit = max(max\_profit, sell\_price - buy\_price).
    

**Complexity:**

*   **Time Complexity:** $O(n^2)$ — Two nested loops iterating through the array.
    
*   **Space Complexity:** $O(1)$ — Only one variable used for max profit.
    

### 2\. Optimal Approach (Two Pointers / Sliding Window)

Instead of checking every pair, we can maintain a "minimum price" seen so far and calculate the profit relative to that minimum.

*   2\. If the sell price is lower than our buy price, it means we found a new local minimum. We move our buy pointer to the sell position.3. If the sell price is higher, we calculate the profit and update max\_profit if it's the highest we've seen.4. Move the sell pointer forward regardless.
    
*   **Dry Run:**
    
    *   prices = \[7, 1, 5, 3, 6, 4\]
        
    *   Day 1 (Buy 7, Sell 1): $1 < 7$, so move buy to Day 2 (Price 1).
        
    *   Day 3 (Buy 1, Sell 5): Profit = 4. max\_profit = 4.
        
    *   Day 5 (Buy 1, Sell 6): Profit = 5. max\_profit = 5.
        

**Complexity:**

*   **Time Complexity:** $O(n)$ — We scan the array exactly once.
    
*   **Space Complexity:** $O(1)$ — Constant space used for pointers and profit variable.