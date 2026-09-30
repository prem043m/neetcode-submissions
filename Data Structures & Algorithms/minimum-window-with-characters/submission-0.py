class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        t_count = Counter(t)
        wind_count = {}
        required = len(t_count)
        formed = 0
        
        left = 0
        min_len = float("inf")
        ansLeft ,ansRight = 0,0

        for right in range(len(s)):
            char = s[right]
            wind_count[char] = wind_count.get(char,0)+1

            if char in t_count and t_count[char] == wind_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                left_char = s[left]
            
                if right-left+1 < min_len :
                    min_len = right-left+1
                    ansLeft = left
                    ansRight = right

                wind_count[left_char] -= 1

                if left_char in t_count and t_count[left_char] > wind_count[left_char]:
                    formed -= 1
                left += 1
        return s[ansLeft:ansRight+1] if min_len != float('inf') else ""


