#https://leetcode.com/problems/range-sum-query-immutable/description/
class NumArray:  

    def __init__(self, nums: List[int]):
        self.preSum = nums  
        for i in range(len(nums)-1):
            self.preSum[i+1] += self.preSum[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0: return self.preSum[right]
        return self.preSum[right] - self.preSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

'''
Analysis
Time Complexity: O(n) 
Since line 7 takes O(n) time and all the other steps take O(1) time.

Space Complexity: O(1) 
This is because self.preSum is a new reference pointing to nums, which isn't creating a new array.
(Python has pass by assignment).
If nums is copied over into a new array, the space will be O(n).
'''