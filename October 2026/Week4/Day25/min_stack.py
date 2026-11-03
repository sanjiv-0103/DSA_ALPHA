class MinStack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        smallest=self.stack[0]
        for num in self.stack:
            if num<smallest:
                smallest=num
        return smallest