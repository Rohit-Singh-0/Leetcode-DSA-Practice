[203\. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)
===============================================================================================

📝 Problem Description
----------------------

Given the head of a linked list and an integer val, remove all the nodes of the linked list that have ListNode.val == val, and return the new head.

💡 Thought Process
------------------

### 1\. Pointer Manipulation

Unlike arrays, removing an element from a linked list doesn't require shifting. We simply "skip" the node by pointing the next pointer of the previous node to the next pointer of the current node.

### 2\. Handling the Head

The trickiest part is when the nodes to be removed are at the start of the list.

*   2\. Once the head is settled, use a temp pointer to traverse the rest of the list.3. If temp.next has the target value, update temp.next to temp.next.next.4. Otherwise, just move temp forward.
    

**Complexity:**

*   **Time Complexity:** $O(n)$ — We traverse the list exactly once.
    
*   **Space Complexity:** $O(1)$ — We only use a few pointer variables.