#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in found:
                return [found[diff], idx]
            found[num] = idx 
        
        return [-1, -1]
        
'''
Analysis
Time Complexity: O(n) 
Since iterating through all n values in nums, dict lookup and add is O(1). 

Space Complexity: O(n) 
All n values of num are stored in nums in the worst case. 
'''