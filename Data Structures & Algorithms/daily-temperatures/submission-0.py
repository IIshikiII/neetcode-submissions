class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                val, val_id = stack.pop()
                res[val_id] = idx - val_id
            stack.append((t, idx))
        return res