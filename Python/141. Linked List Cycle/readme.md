[141\. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
===========================================================================

📝 Problem Description
----------------------

Given head, the head of a linked list, determine if the linked list has a cycle in it. A cycle exists if there is some node in the list that can be reached again by continuously following the next pointer.

💡 Thought Process
------------------

### 1\. Hash Set Approach (Linear Space)

*   **Logic:** Iterate through the list and store each node's memory address (or the node object itself) in a hash set. If we encounter a node that is already in the set, a cycle exists.
    
*   **Complexity:**
    
    *   **Time Complexity:** $O(n)$
        
    *   **Space Complexity:** $O(n)$ — We store up to $n$ nodes in the set.
        

### 2\. Floyd's Tortoise and Hare (Optimal Space)

This is a "Two-Pointer" technique specifically for linked lists.

*   2\. Move slow by one step and fast by two steps.3. If there is a cycle, the fast pointer will eventually "lap" the slow pointer, and they will meet at the same node.4. If fast reaches the end (None), there is no cycle.
    
*   **Complexity:**
    
    *   **Time Complexity:** $O(n)$
        
    *   **Space Complexity:** $O(1)$ — Only two pointers are used regardless of list size.