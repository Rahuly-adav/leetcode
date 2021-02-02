# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        #Brute Force creating new linklist using reversed array
        a=[]
        node=None
        new=None
        while head:
            a.append(head.val)
            head=head.next
        for i in a[::-1]:
            if not new:
                new=ListNode(i)
                node=new
            else:
                new.next=ListNode(i)
                new=new.next
        return node"""
        #-----------------------------
        """#adding elements in front of linklist
        new=node=None
        while head:
            if not node:
                print("hello",head.val)
                node=ListNode(head.val)
            else:
                fre=ListNode(head.val)
                fre.next=node
                node=fre
            head=head.next
        return node"""
        #----------------------------------------
        #reversing the same linklist using iteration
        """pre=None
        while head:
            cur=head
            head=head.next
            cur.next=pre
            pre=cur
        return pre"""
        #--------------------------------------
        #reversing the same linklist using Recursion
        if not head or not head.next: return head
        node, head.next.next, head.next = self.reverseList(head.next), head, None
        return node