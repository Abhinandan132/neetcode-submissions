class MinStack:

    def __init__(self):
        self.s = [] 

    def push(self, val: int) -> None:
        if (not self.s): 
            self.min_val = val 
        else: 
            self.min_val = min(val, self.s[-1][1])
        self.s.append((val, self.min_val))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0] 

    def getMin(self) -> int:
        return self.s[-1][1]
