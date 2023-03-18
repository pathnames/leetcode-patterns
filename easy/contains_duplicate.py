#https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = collections.Counter()
        for num in nums: 
            cnt[num] += 1
            if cnt[num] == 2: 
                return True 
        
        return False 

#Analysis
'''
Time Complexity: O(n)
Since Counter is a dictionary with O(1) add/delete/lookup, and n items are being added.
Space Complexity: O(n) since dictionary will add at most n elements.
'''