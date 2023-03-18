#https://leetcode.com/problems/linked-list-cycle/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head 
        while fast and fast.next: 
            fast = fast.next.next 
            slow = slow.next 
            if fast == slow: 
                return True
        return False

'''
Analysis
Time Complexity: O(n) 
Since iterating through all n nodes of linked-list. 

Space Complexity: O(1) 
Only memory created is 2 pointers. 
'''