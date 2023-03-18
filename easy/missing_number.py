#https://leetcode.com/problems/missing-number/description/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumN = (n * (n + 1)) // 2 
        sumNums = 0
        for num in nums: sumNums += num 
        return sumN - sumNums

'''
Analysis
Time Complexity: O(n) 
Since line 7 takes O(n) time and all the other steps take O(1) time.

Space Complexity: O(1)
'''