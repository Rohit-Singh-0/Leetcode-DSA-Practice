[344\. Reverse String](https://leetcode.com/problems/reverse-string/)
=====================================================================

📝 Problem Description
----------------------

Write a function that reverses a string. The input string is given as an array of characters s. You must do this by modifying the input array **in-place** with $O(1)$ extra memory.

💡 Thought Process
------------------

### 1\. Two Pointer Approach (Optimal)

Since we need to reverse the array in-place, we can swap elements from the outside in.

*   2\. While the left pointer is less than the right pointer:
    
    *   Swap the characters at s\[l\] and s\[r\].
        
    *   Increment l and decrement r.
        
*   **In-place Swap:** Python allows for elegant swapping using s\[l\], s\[r\] = s\[r\], s\[l\] without needing a temporary variable.
    

**Complexity:**

*   **Time Complexity:** $O(n)$ — We visit each element exactly once (specifically $n/2$ swaps).
    
*   **Space Complexity:** $O(1)$ — No additional data structures are used; the reversal happens within the original memory space.