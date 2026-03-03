# [1\. Two Sum](https://leetcode.com/problems/two-sum/)

## 📝 Problem Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

## 💡 Thought Process

### 1\. Brute Force Approach

The simplest way to solve this is to check every possible pair of numbers in the array.

- **Logic:** Use nested loops. The outer loop picks an element, and the inner loop checks all subsequent elements to see if their sum equals the target.
- **Dry Run:** - nums = \[2, 7, 11, 15\], target = 9
  - When i = 0 (nums\[i\] = 2), the inner loop checks j = 1 (nums\[j\] = 7).
  - $2 + 7 = 9$, which matches the target. Return \[0, 1\].

**Complexity:**

- **Time Complexity:** $O(n^2)$ — In the worst case, we traverse the array $n$ times for every element.
- **Space Complexity:** $O(1)$ — No additional data structures are used.

### 2\. Optimal Approach (Hash Map)

To improve performance, we can use a Hash Map (dictionary) to trade space for time. This allows us to find the "complement" of the current number in constant time.

- **Logic:** As we iterate through the array, we calculate the remainder (target - current number). If the current number already exists in our map, it means we previously found its partner. If not, we store the remainder as a key and the current index as the value for future reference.
- **Dry Run:**
  - nums = \[2, 7, 11, 15\], target = 9, remainder_map = {}
  - i = 0: nums\[0\] = 2. Not in map. Store remainder ($9 - 2 = 7$) with index: {7: 0}.
  - i = 1: nums\[1\] = 7. This **is** in the map!
  - Return current index 1 and stored index 0 $\\rightarrow$ \[1, 0\].

**Complexity:**

- **Time Complexity:** $O(n)$ — We only traverse the list once.
- **Space Complexity:** $O(n)$ — In the worst case, we store $n$ elements in the hash map.
