# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''cur=node=head
        ans=None
        if not head:
            return head
        if not head.next:
            return head
        cur=cur.next
        a=None
        while cur:
            
            if node.val!=cur.val:
                if not ans:
                    a=ListNode(node.val)
                    ans=a
                else:
                    a.next=ListNode(node.val)
                    a=a.next
                node=cur
            cur=cur.next
        if a:
            if a.val!=node.val:
                a.next=ListNode(node.val)
                a=a.next
        else:
            a=ListNode(node.val)
            ans=a
        return ans'''
        if not head:
            return head
        if not head.next:
            return head
        pre=cur=root=head
        cur=cur.next
        while cur:
            if cur.val==pre.val:
                pre.next=cur.next
            else:
                pre=pre.next
            cur=cur.next
        return root
        