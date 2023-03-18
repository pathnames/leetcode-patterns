#https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = collections.deque()
        q.append(root)
        ans = []

        while q: 
            size = len(q)
            level_sum = 0
            for _ in range(size): 
                curNode = q.popleft()
                level_sum += curNode.val
                if curNode.left: q.append(curNode.left)
                if curNode.right: q.append(curNode.right)
            ans.append(level_sum / size)

        return ans

'''
Analysis
Time Complexity: O(n) 
Since iterating through all n nodes of tree using level order traversal.

Space Complexity: O(m) where m = level with most nodes since at most m nodes will be stored in queue.
'''