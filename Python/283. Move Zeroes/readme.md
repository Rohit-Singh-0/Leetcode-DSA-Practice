[283\. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
===============================================================

📝 Problem Description
----------------------

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. You must do this **in-place** without making a copy of the array.

💡 Thought Process
------------------

### 1\. Two-Pointer Approach (Optimal)

To achieve $O(1)$ space complexity, we use two pointers to reorganize the array as we traverse it.

*   2\. Pointer j (the "Fast" pointer) iterates through the array to find non-zero elements.3. If nums\[i\] is zero and nums\[j\] is non-zero, we swap them and move the i pointer forward.4. If nums\[i\] is already a non-zero number, we simply move i forward to find the next zero.5. The j pointer moves forward in every iteration.
    
*   **Complexity:**
    
    *   **Time Complexity:** $O(n)$ — We visit each element in the array exactly once.
        
    *   **Space Complexity:** $O(1)$ — No extra memory is allocated; all swaps happen within the input array.