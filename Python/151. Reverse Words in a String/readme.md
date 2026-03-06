[151\. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)
===========================================================================================

📝 Problem Description
----------------------

Given an input string s, reverse the order of the words. A word is defined as a sequence of non-space characters. Your solution must handle multiple spaces between words and leading/trailing whitespace.

💡 Thought Process
------------------

### 1\. Manual Parsing (The Logic-First Approach)

Instead of relying on high-level split functions, we manually extract words to demonstrate a deep understanding of string traversal.

*   2\. If the character is alphanumeric, build the current word.3. If we hit a space, append the word to our words list (if the word isn't empty).4. **Corner Case:** Ensure the last word is appended if the string doesn't end in a space.
    
*   **Complexity:**
    
    *   **Time Complexity:** $O(n)$ — Single linear scan.
        
    *   **Space Complexity:** $O(n)$ — To store the extracted words.
        

### 2\. Pythonic Built-in Approach

*   **Logic:** Use .split() which handles all whitespace edge cases (multiple spaces, leading/trailing) automatically. Reverse the resulting list and join with a single space.