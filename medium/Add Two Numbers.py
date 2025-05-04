# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next 


# 5ms runtime, beats 76%
class Solution(object): 
    def addTwoNumbers(self, l1, l2):
        ptr1 = l1
        ptr2 = l2
        mult = 1
        node = ListNode(0)
        node_ptr = node
        carry = 0
        while ptr1 or ptr2 or carry:
            val1 = ptr1.val if ptr1 else 0
            val2 = ptr2.val if ptr2 else 0
            to_add = val1+val2+carry
            node.next = ListNode(to_add%10)
            node = node.next
            mult *= 10
            carry, wtv = divmod(to_add, 10)
            ptr1 = ptr1.next if ptr1 else ptr1
            ptr2 = ptr2.next if ptr2 else ptr2         
                
        return node_ptr.next
        
