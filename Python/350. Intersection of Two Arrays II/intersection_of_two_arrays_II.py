from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        list1 = Counter(nums1)
        list2 = Counter(nums2)
        if len(list1) <= len(list2):
            short, longer = list1, list2
        else:
            short, longer = list2, list1
        for i in short:
            if i in longer:
                ans += [i]*min(short[i], longer[i])
        return ans
        
        # return list((Counter(nums1) & Counter(nums2)).elements())