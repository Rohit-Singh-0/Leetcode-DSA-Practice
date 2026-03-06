[242\. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
===================================================================

📝 Problem Description
----------------------

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

💡 Thought Process
------------------

### 1\. Brute Force (Nested Count)

*   **Logic:** Iterate through string s and for each character, compare its frequency in both s and t using the built-in .count() method.
    
*   **Complexity:** - **Time:** $O(n^2)$ because .count() is an $O(n)$ operation inside an $O(n)$ loop.
    
    *   **Space:** $O(1)$.
        

### 2\. Manual Hash Map (Optimal)

*   **Logic:** Create two frequency dictionaries. We use the .get(char, 0) method to handle new characters safely. By comparing the two dictionaries, we ensure all characters and their counts match.
    
*   **Complexity:** - **Time:** $O(n)$ where $n$ is the length of the strings.
    
    *   **Space:** $O(k)$ where $k$ is the character set size (max 26 for English).
        

### 3\. Pythonic Solution (collections.Counter)

*   **Logic:** Counter is a subclass of dict designed for counting hashable objects. It simplifies the code significantly while maintaining the same $O(n)$ efficiency.