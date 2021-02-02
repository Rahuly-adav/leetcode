# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return l1
        elif not l2 or not l1:
            return l1 if l1 else l2
        temp=None
        ans=None
        while l1 and l2:
            if l1.val<=l2.val:
                if not ans:
                    temp=ListNode(l1.val)
                    ans=temp
                else:
                    temp.next=ListNode(l1.val)
                    temp=temp.next
                l1=l1.next
            else:
                if not ans:
                    temp=ListNode(l2.val)
                    ans=temp
                else:
                    temp.next=ListNode(l2.val)
                    temp=temp.next
                l2=l2.next
        temp.next=l1 if l1 else l2
        return ans