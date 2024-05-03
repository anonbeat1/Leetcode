from typing import Optional

          
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def __init__(self):
        self.headList = ListNode()

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        return self.reverse(head,None)

    def reverse(self,node,prev_node):
        if node:
            next_node = node.next
            node.next = prev_node
            return self.reverse(next_node,node)
        else:
            return prev_node

    
    def append(self,data):
        new_node = ListNode(data)
        current_node = self.headList
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def pprint(self):
        current_node = self.headList
        lista = list()
        while current_node:
            current_node = current_node.next
            lista.append(current_node.val)
        return lista

x = Solution()
list_to_reverse = [1,2,3,4,5,6]
for data in list_to_reverse:
    x.append(data)

print(x.reverseList(x.headList))

