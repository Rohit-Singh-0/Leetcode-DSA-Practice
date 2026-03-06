[904\. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)
=============================================================================

📝 Problem Description
----------------------

You are visiting a farm that has a single row of fruit trees. You have **two baskets**, and each basket can only hold a **single type** of fruit. Starting from any tree of your choice, you must collect as much fruit as possible while moving to the right, stopping when you reach a tree with a third type of fruit.

💡 Thought Process
------------------

### 1\. The Core Challenge

The problem is essentially asking: _"Find the longest contiguous subarray that contains at most two distinct integers."_

### 2\. Why Simple Lists Fail

Initial attempts using list.pop(0) or set(list) inside a loop lead to $O(n^2)$ time complexity. In an SDE context, we need to handle potentially millions of trees, so we must achieve $O(n)$.

### 3\. Optimal Approach: Sliding Window

*   2\. Use a hash map (count) to track the frequency of each fruit type in the current window.3. Expand the window by moving r.4. If the number of distinct types (size of hash map) exceeds 2, shrink the window from the left (l) until we are back to 2 types.5. Keep track of the maximum total (window size) seen so far.
    

**Complexity:**

*   **Time Complexity:** $O(n)$ — Each fruit is visited by the r pointer once and the l pointer at most once.
    
*   **Space Complexity:** $O(1)$ — Since the hash map will never contain more than 3 keys at any time.