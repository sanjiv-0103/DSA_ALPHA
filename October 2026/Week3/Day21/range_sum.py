class NumArray:
    def __init__(self,nums): #initializing the constructor
        self.nums=nums #storing the input list
    def sum_range(self,left,right): #calculating the sum of elements in gvn range
        total=0
        for i in range(left,right+1): #this loop iterates through the elements 
            total+=self.nums[i] #adds them to the total
        return total
#obj=NumArray(nums)
#print(obj.sum_range(0,2))