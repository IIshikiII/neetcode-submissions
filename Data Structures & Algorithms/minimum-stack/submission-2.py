class MinStack:

    def __init__(self):
        self.min_vals = []
        self.min_val = None
        self.min_ids = []
        self.min_id = None
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_val is None:
            self.min_idx = 0
            self.min_val = val
            self.min_vals.append(self.min_val)
            self.min_ids.append(self.min_id)
        elif val < self.min_val:
            self.min_idx = len(self.stack) - 1
            self.min_val = val
            self.min_vals.append(self.min_val)
            self.min_ids.append(self.min_id)
        elif val >= self.min_val:
            self.min_vals.append(self.min_val)
            self.min_ids.append(self.min_id)    
    def pop(self) -> None:
            val = self.stack.pop(-1)
            self.min_vals.pop(-1)
            self.min_ids.pop(-1)
            if val == self.min_val and len(self.min_vals) >= 1:
                self.min_val = self.min_vals[-1]
                self.min_id = self.min_ids[-1]
            elif val == self.min_val and len(self.min_vals) == 0:
                self.min_val = None
                self.min_id = None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_val
        
