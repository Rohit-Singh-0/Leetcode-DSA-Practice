class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # brute force
        for i in range(len(nums)): #traverse the array nums from 0 to len(nums)
            for j in range(i+1, len(nums)): #then with the previous value of i traverse the array nums again from i+1 to len(nums) to consider only the element other than at index i
                if nums[i] == nums[j]: #if the elements in array nums at index i and index j are same then there is a duplicate so return True
                    return True
        return False # else after the for loop ends and no duplicate was found then return False

        #time = O(n^2)
        #space = O(1)

        #opitmal approach - using a set
        seen = set() #creating an empty set to store the seen values from nums array in it for later reference
        for i in nums:# traverse the array nums using a for loop
            if i in seen: # if the current element from nums is in the seen set then it is a duplicate hence return True
                return True
            seen.add(i) # otherwise add the current element in the seen set
        return False # after the for loop ends meand that no duplicate was found hence return False

        #time = O(n)
        #space = O(n)