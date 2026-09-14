class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        for i , temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_val,prev_idx = stack.pop()
                res[prev_idx] = i-prev_idx
            stack.append((temp,i))
        return res