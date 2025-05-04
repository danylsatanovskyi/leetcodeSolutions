# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#most optimal solution, O(m+n) time complexity, where m and n are the lengths of the two linked lists

class Solution(object):
    def mergeTwoLists(self, list1, list2):

            if not list1:
                return list2
            if not list2:
                return list1

            head = list1 if list1.val<=list2.val else list2

            node = head

            if head == list1:
                list1 = list1.next
            else:
                list2 = list2.next

            while list1 and list2:
                if list1.val<=list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next


                node = node.next
            
            if list2:
                node.next = list2
            else:
                node.next = list1

            return head
                

      
