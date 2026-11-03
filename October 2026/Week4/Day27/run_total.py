class Move_Avg:
    def __init__(self,size):
        self.size=size
        self.arr=[]
        self.total=0
    def next(self,val):
        self.arr.append(val)
        self.total+=val
        if len(self.arr)>self.size:
            old=self.arr[0]
            del self.arr[0]
            self.total-=old
        return self.total/len(self.arr)