class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ### Two Pointer approach:
        n = len(heights)
        left = 0
        right = n-1
        max_water = 0
        while left < right :
            width = right-left
            minHeight = min(heights[left],heights[right])
            curr_water = width*minHeight
            max_water = max(curr_water,max_water)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_water
        # ### brute Force:
        # n = len(heights)
        # maxWater = 0

        # for i in range(n):
        #     for j in range(i+1,n):
        #         width = j-i
        #         minheight = min(heights[i],heights[j])
        #         maxWater = max(maxWater,minheight*width)
        # return maxWater