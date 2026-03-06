class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute force
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        #time = O(n^2)
        #space = O(1)
        '''In this brute force approach I traverse the elements of the array and then check for every combination of other elements after the current elements index and return both the index if the sum of elements at these 2 indexes is equal to the target. This approach traverse the array n(length of array) times for every element so the time complexity is O(n^2) and there is no storing of elements in any data structure hence the space complexity is (1)

        for example nums = [2,7,11,15], target = 9
        if i = 0 nums[i] = 2
        for this current value the algorithm will check for nums[j] where j =[1,2,3]
        nums[i]+nums[j] == nums[0] + nums[1] == 2+7 == target=9:
        hence it will return the indexes [0,1]

        
        '''


        #Optimal solution - using hashmap
        remainder_map = {} # initialise empty hashmap
        for index, num in enumerate(nums): # traverse every element in the array using a for loop
            if num in remainder_map: #if the current num is in the hashmap then run the following indented code
                return [index, remainder_map[num]] # return the index of the current num and the index we saved in the hashmap previously along with the remanider
            remainder_map[target-num] = index # if the num is not in hashmap then store the remainder(target-num) in the hashmap along with index in a key value pair
        #time = O(n)
        #space = O(n)
        '''In this optimal approach I leverage the hashmap to store the remainder value and the index for the current num that we have from the array and if we encounter that remainder value further in the array we return the index of the current num and the index stored in the hashmap else we store the remainder(target-num) and the current index to reference for a further value in the array
        
        for example nums = [2,7,11,15], target = 9
        h_map= {}
        i = 0
        h_map is empty and nums[0] not in h_map
        h_map = {remainder:index} = {target-num: index} = {9-2:0} = {7:0}
        now i =1 nums[1] == 7
        and 7 is present in h_map
        hence return the current and h_map indexes = [1,0]
        '''