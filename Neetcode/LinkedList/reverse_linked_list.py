# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        traverse = head
        previous = None

        while traverse:
            temp = traverse.next
            traverse.next = previous
            previous = traverse
            traverse = temp
        
        return previous

        