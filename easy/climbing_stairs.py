#https://leetcode.com/problems/climbing-stairs/

#Recursive solution
class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n):  
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n-1) + climb(n-2)
                return memo[n]
        memo = {1: 1, 2: 2} 
        return climb(n)

'''
Analysis
Time Complexity: O(n) 
Same as fibonacci.

Space Complexity: O(n) 
All n values are stored. 
'''

#Iterative Solution 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

'''
Analysis
Time Complexity: O(n) 
Same as fibonacci.

Space Complexity: O(n) 
All n values are stored. 
'''
