class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #brute force
        # val = float("inf")
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)+1):
        #         # print([i,j], nums[i:j])
        #         if sum(nums[i:j+1]) >= target:
        #             val = min(val, j-i+1)
        #             # print(nums[i:j])
        # if val == float("inf"):
        #     return 0
        # else:
        #     return val

        #optimal solution
        l =0
        curr_sum = 0
        #  = 0
        res = float("inf")
        for r in range(len(nums)):
            curr_sum += nums[r]
            # print([curr_sum, nums[r]])
            if curr_sum >= target:
                # print("curr_sum greater than equal to target")
                res = min(res, r-l+1)
                # print("result:", res, nums[l:r+1])
                while curr_sum >= target:
                    # print(nums[l:r+1], curr_sum)
                    res = min(res, r-l+1)
                    curr_sum -= nums[l]
                    l+=1
                    
                    # print(curr_sum, nums[l:r+1])
        if res == float("inf"):
            return 0
        return res
            