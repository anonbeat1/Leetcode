#Definition for singly-linked list.
from typing import Optional

          
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def __init__(self):
        self.headList = ListNode()
        self.reversedList = ListNode()

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        current_node = head
        while current_node is not None:
            next_node = current_node.next            
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node
       
    def append(self,data):
        new_node = ListNode(data)
        current_node = self.headList
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def pprint(self):
        current_node = self.headList
        node_list = list()
        while current_node.next is not None:
            current_node = current_node.next
            node_list.append(current_node.val)
        return node_list
    
    
            
    
x = Solution()
list_to_reverse = [1,2]
for data in list_to_reverse:
    x.append(data)

print(x.reverseList(x.headList))
print(x.pprint())

