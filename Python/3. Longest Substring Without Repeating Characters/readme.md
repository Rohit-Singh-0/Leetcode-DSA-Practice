[3\. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
===================================================================================================================================

📝 Problem Description
----------------------

Given a string s, find the length of the **longest substring** without repeating characters.

💡 Thought Process
------------------

### 1\. Sliding Window Technique

Since we are looking for a **contiguous substring**, a sliding window is the most efficient approach.

*   2\. Use a set to store the unique characters currently in the window.3. Expand the window by moving r and adding s\[r\] to the set.4. If s\[r\] is already in the set, it means we have a duplicate. Shrink the window from the left (l) and remove characters from the set until the duplicate is gone.5. Update the maximum length found so far (val).
    

**Complexity:**

*   **Time Complexity:** $O(n)$ — Each character is added to and removed from the set at most once.
    
*   **Space Complexity:** $O(min(n, m))$ — Where $n$ is the length of the string and $m$ is the size of the character set (e.g., 26 for English letters, 128 for ASCII).