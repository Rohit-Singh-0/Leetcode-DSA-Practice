import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force
        if len(s) != len(t):
            return False
        for i in s:
            if s.count(i) != t.count(i):
                return False
        return True
        #time = O(n^2)
        #space = O(1)


        #optimal solution - using hashmaps
        if len(s) != len(t):
            return False
        char_count_s = {}
        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) +1
        char_count_t = {}
        for char in t:
            char_count_t[char] = char_count_t.get(char , 0) +1
        if char_count_s == char_count_t:
            return True
        return False
        #time = O(n+m) = O(n), where n = len(s) and m = len(t) here n = m
        #space = O(k) kmax = 26 english albhabets

        #using collections.Counter library
        return collections.Counter(s) == collections.Counter(t)
        #time = O(n+m) = O(n), where n = len(s) and m = len(t) here n = m
        #space = O(k) kmax = 26 english albhabets