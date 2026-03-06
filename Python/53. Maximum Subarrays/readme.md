[53\. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
========================================================================

📝 Problem Description
----------------------

Given an integer array nums, find the subarray with the largest sum and return its sum.

💡 Thought Process
------------------

### 1\. Brute Force (Cubic Time)

*   **Logic:** Iterate through every possible starting point i and ending point j, then calculate the sum of that subarray.
    
*   **Complexity:**
    
    *   **Time Complexity:** $O(n^3)$ — Two loops for boundaries and one hidden loop for sum().
        
    *   **Space Complexity:** $O(1)$.
        

### 2\. Kadane's Algorithm (Optimal)

Instead of recomputing sums, we make a local decision at each element.

*   2\. For each new number, decide: Is it better to add the number to the existing curr\_sum, or start a fresh subarray from this number?3. Formula: curr\_sum = max(current\_element, curr\_sum + current\_element).
    
*   **Complexity:**
    
    *   **Time Complexity:** $O(n)$ — Single pass through the array.
        
    *   **Space Complexity:** $O(1)$ — Only two variables used regardless of input size.