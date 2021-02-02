# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a={}
        i=1
        while headA:
            a[headA]=i
            headA=headA.next
            i+=1
        while headB:
            if headB in a:
                return headB
            headB=headB.next