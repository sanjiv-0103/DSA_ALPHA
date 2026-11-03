class MaxStack:
    def __init__(self):
        self.stack=[]
        self.max_stack=[]
    def push(self,value):
        self.stack.append(value)
        if len(self.max_stack)==0 or value>=self.max_stack[-1]:
            self.max_stack.append(value)
    def pop(self):
        value=self.stack.pop()
        if value==self.max_stack[-1]:
            self.max_stack.pop()
    def top(self):
        return self.stack[-1]
    def getMax(self):
        return self.max_stack[-1]
s=MaxStack()