class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if not self.minstack:
            min_val = val
        else:
            min_val = self.minstack[-1] if self.minstack[-1] < val else val
        self.stack.append(val)
        self.minstack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
