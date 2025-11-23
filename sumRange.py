class NumArray:

    def __init__(self, nums: list[int]):
        self.nums=nums

    def sumRange(self, left: int, right: int) -> int:
        result=0
        for i in range(left,right+1):
            result+=self.nums[i]

        return result
        

# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2,0,3,-5,2,-1])
print(obj.sumRange(0, 5))
print(obj.sumRange(2, 5))