class MyQueue:
    def __init__(self):
        self.input=[]
        self.output=[]
    def push(self,value):
        self.input.append(value)
    def move(self):
        if len(self.output)==0:
            while len(self.input)>0:
                self.output.append(self.input.pop())
    def pop(self):
        self.move()
        return self.output.pop()
    def peek(self):
        self.move()
        return self.output[-1]
    def empty(self):
        return len(self.input)==0 and len(self.output)==0
q=MyQueue()
q.push(10)
q.push(20)
q.push(30)
print(q.pop())
print(q.peek())
print(q.empty())