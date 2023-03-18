#https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        nodes = []
        q = collections.deque()
        q.append(root)
        while q: 
            level = []
            for i in range(len(q)):
                curNode = q.popleft()
                level.append(curNode.val)
                if curNode.left: 
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
            nodes.append(level)
        
        return nodes 
            

'''
Analysis
Time Complexity: O(n) 
Since exploring all n nodes in tree. 

Space Complexity: O(n) 
All n values of nodes are stored in a list. 
'''