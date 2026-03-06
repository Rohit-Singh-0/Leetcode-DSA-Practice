class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #brute force 
        res = nums[0]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                res = max(res, sum(nums[i:j]))
        return res

        #Optimized solution
        res = nums[0]
        curr = nums[0]
        for num in range(1, len(nums)):
            curr = max(nums[num], curr+nums[num])
            res = max(res, curr)
        return res