class ListNode:
	def __init__(self,val=0,next=None):
		self.val = val
		self.next = next
		
class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.count = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.count:
              return -1      
        current_node = self.head.next
        for _ in range(index):
              current_node = current_node.next
        return current_node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.count,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        current_node.next = ListNode(val,current_node.next)
        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count:
            return
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        next_node = current_node.next
        current_node.next = next_node.next #Skippo uno
        next_node.next = None
        self.count -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)