class MaxStack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def getMax(self):
        biggest=self.stack[0]
        for num in self.stack:
            if num>biggest:
                biggest=num
        return biggest