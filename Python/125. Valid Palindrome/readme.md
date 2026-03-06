125. Valid Palindrome
📝 Problem Description
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
💡 Thought Process
1. Filter and Reverse (Linear Space)
Logic: Create a temporary string by iterating through the input and keeping only lowercase alphanumeric characters. Compare this string to its reverse.
Complexity:
Time Complexity: $O(n)$
Space Complexity: $O(n)$ — We create a new string of size up to $n$.


2. Two Pointer Approach (Optimal Space)
2. If a pointer lands on a non-alphanumeric character, skip it.3. If both land on alphanumeric characters, compare them (ignoring case).4. If they don't match, return False.5. Move pointers closer and repeat until they meet.
Complexity:
Time Complexity: $O(n)$ — Each character is visited at most once.
Space Complexity: $O(1)$ — No extra strings or lists are created; the check is done in-place.





