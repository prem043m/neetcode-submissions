class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ### optimal:
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j,k = i+1,n-1
            while j < k:
                curr_sum = nums[i] + nums[j]+ nums[k]
                if curr_sum < 0:
                    j += 1
                elif curr_sum > 0:
                    k -= 1
                else:
                    res.append([nums[i],nums[j],nums[k]])

                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res

        ### better apporch:
        # n = len(nums)
        # res = []
        # UT = set()

        # for i in range(n):
        #     s = set()
        #     target = -nums[i]
        #     for j in range(i+1,n):
        #         third = target - nums[j]
                
        #         if third in s:
        #             trip = tuple(sorted([nums[i],nums[j],third]))
        #             UT.add(trip)
        #         s.add(nums[j])
        # return [list(t) for t in UT]

        ### Brute Force (simpler method):
        # n = len(nums)
        # res = []
        # s = set()

        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 trip = sorted([nums[i],nums[j],nums[k]])
        #                 # to convert trip into tuple bcs list are muttable and tuple is not so
        #                 trip_tuple = tuple(trip)
        #                 if trip_tuple not in s:
        #                     s.add(trip_tuple)
        #                     res.append(trip)
        # return res