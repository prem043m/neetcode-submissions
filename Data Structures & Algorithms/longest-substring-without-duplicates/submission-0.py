class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_set = set()
        left = 0
        maxSeq = 0
        for right in range(len(s)):
            while s[right] in unique_set:
                unique_set.remove(s[left])
                left += 1
            unique_set.add(s[right])
            maxSeq = max(maxSeq,right-left+1)
        return  maxSeq
