[217\. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
=============================================================================

📝 Problem Description
----------------------

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

💡 Thought Process
------------------

### 1\. Brute Force Approach

The naive approach is to compare every element with every other element in the array.

*   **Logic:** Use a nested loop. The outer loop picks an element at index i, and the inner loop checks all subsequent elements at index j. If nums\[i\] == nums\[j\], a duplicate exists.
    
*   **Complexity:**
    
    *   **Time Complexity:** $O(n^2)$ — Due to the nested iteration.
        
    *   **Space Complexity:** $O(1)$ — No extra memory used.
        

### 2\. Optimal Approach (Hash Set)

We can use a **Set** data structure to keep track of the numbers we have already encountered.

*   2\. Iterate through the array.3. For each number, check if it already exists in seen.4. If it does, we've found a duplicate—return True immediately.5. If not, add the number to the set and continue.6. If the loop finishes without finding a duplicate, return False.
    
*   **Why it works:** Searching in a set (hash table) takes $O(1)$ on average, allowing us to finish the check in a single pass.
    

**Complexity:**

*   **Time Complexity:** $O(n)$ — We iterate through the list only once.
    
*   **Space Complexity:** $O(n)$ — In the worst case (no duplicates), we store all $n$ elements in the set.