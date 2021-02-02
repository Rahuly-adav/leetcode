# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """b,a,node="","",None
        while l1:
            a+=str(l1.val)
            l1=l1.next
        while l2:
            b+=str(l2.val)
            l2=l2.next
        c=str(int(a[::-1])+int(b[::-1]))
        for i in c[::-1]:
            if not node:
                new=ListNode(i)
                node=new
            else:
                new.next=ListNode(i)
                #node.next=new
                new=new.next
        return node"""
        node=None
        c=0
        while l1 and l2:
            if not node:
                a=l1.val+l2.val
                if a>9:
                    c=1
                    new=ListNode(str(a)[1])
                else:
                    new=ListNode(a)
                node=new
            else:
                a=l1.val+l2.val+c
                c=0
                if a>9:
                    c=1
                    new.next=ListNode(str(a)[1])
                else:
                    new.next=ListNode(a)
                new=new.next
            l1=l1.next
            l2=l2.next
        while l1:
            a=l1.val+c
            c=0
            if a>9:
                c=1
                new.next=ListNode(str(a)[1])
            else:
                new.next=ListNode(a)
            new=new.next
            l1=l1.next
        while l2:
            a=l2.val+c
            c=0
            if a>9:
                c=1
                new.next=ListNode(str(a)[1])
            else:
                new.next=ListNode(a)
            new=new.next
            l2=l2.next
        if c==1:
            new.next=ListNode(1)
            new=new.next
        return node