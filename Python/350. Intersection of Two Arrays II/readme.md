[350\. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
===================================================================================================

📝 Problem Description
----------------------

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays.

💡 Thought Process
------------------

### 1\. Hash Map (Frequency Counter) Approach

Unlike "Intersection I" (where we only care about unique elements), this problem requires us to track how many times each number appears.

*   2\. To optimize, identify the smaller dictionary (short) to reduce the number of iterations.3. For each key in short, check if it exists in longer.4. If it exists, add it to our result list min(count1, count2) times.
    
*   **Complexity:**
    
    *   **Time Complexity:** $O(n + m)$ — We iterate through nums1 to count, nums2 to count, and then through the unique keys of the smaller counter.
        
    *   **Space Complexity:** $O(n + m)$ — In the worst case, we store all elements of both arrays in counters.