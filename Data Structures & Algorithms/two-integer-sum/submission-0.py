class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1 using hashmap 
        prevMap = {}

        for i,num in enumerate(nums):
            diff = target - num
        
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[num] = i 
        return [-1,-1]

        # 2
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(len(nums)):
        #         sum = nums[i] + nums[j]
        #         if sum == target:
        #             return [i,j]
        # return [-1,-1];
