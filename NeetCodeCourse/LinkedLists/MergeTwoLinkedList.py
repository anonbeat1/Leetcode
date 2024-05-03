from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list_head = ListNode()
        head = merged_list_head
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        
        if list1:
            head.next = list1
        else:
            head.next = list2
        return merged_list_head.next
                
       


x = Solution()
x.mergeTwoLists([1,2,3],[1,3,4])