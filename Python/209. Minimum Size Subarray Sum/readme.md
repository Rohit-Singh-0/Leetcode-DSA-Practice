[209\. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
===========================================================================================

📝 Problem Description
----------------------

Given an array of positive integers nums and a positive integer target, return the **minimal length** of a contiguous subarray of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

💡 Thought Process
------------------

### 1\. The Strategy: Variable-Size Sliding Window

Since we need a **contiguous** subarray and the numbers are all **positive**, we can use the sliding window technique. The positivity is key because it ensures that adding an element always increases the sum and removing one always decreases it.

*   2\. As soon as curr\_sum >= target, we have a valid window.3. Now, try to **shrink** the window from the left to see if a smaller subarray also satisfies the condition.4. Record the minimum length (r - l + 1) during this shrinking process.5. Repeat until the right pointer reaches the end.
    

**Complexity:**

*   **Time Complexity:** $O(n)$ — Each element is added and removed from the window exactly once.
    
*   **Space Complexity:** $O(1)$ — Only a few variables are used to track pointers and sums.