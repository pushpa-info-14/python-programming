from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.sums = []
        self.nums = nums
        temp = 0
        for i in nums:
            temp += i
            self.sums.append(temp)

    def sumRange(self, left: int, right: int) -> int:
        return  self.sums[right] - self.sums[left] + self.nums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

obj = NumArray([-2,0,3,-5,2,-1])
print(obj.sumRange(0,2))
print(obj.sumRange(2,5))
print(obj.sumRange(0,5))

obj2 = NumArray([-4,-5])
print(obj2.sumRange(0,0))
print(obj2.sumRange(1,1))
print(obj2.sumRange(0,1))
print(obj2.sumRange(0,0))