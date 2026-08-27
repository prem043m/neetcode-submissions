class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums) 
        curr_streak = 1
        long_streak = 1
        for i in range(1,len(nums)):
            if sorted_nums[i] == sorted_nums[i-1]:
                continue

            if sorted_nums[i]-sorted_nums[i-1] == 1:
                curr_streak += 1
            else:
                long_streak = max(curr_streak,long_streak)
                curr_streak = 1
        return max(long_streak,curr_streak)