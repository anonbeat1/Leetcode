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
		else:        
			current_node = self.head.next   
			for _ in range(index):
				current_node = current_node.next
			return current_node.val

	def addAtHead(self, val: int) -> None:
		self.addAtIndex(0, val)

	def addAtTail(self, val: int) -> None:
		self.addAtIndex(self.count, val)

	def addAtIndex(self, index: int, val: int) -> None:
		if index > self.count: 
			print("Out of Bound Index")
		else:
			current_node = self.head
			for _ in range(index):
				current_node = current_node.next
			current_node.next = ListNode(val,current_node.next)
			self.count += 1

	def deleteAtIndex(self, index: int) -> None:
		if index >= self.count: 
			print("Out of Bound Index")
		else:
			current_node = self.head
			for _ in range(index):
				current_node = current_node.next
			t = current_node.next
			current_node.next = t.next
			t.next = None
			self.count -= 1

			'''
			for _ in range(index):
				prev_node = current_node
				current_node = current_node.next
			prev_node.next = current_node.next'''

	
	def pprint(self):
		current_node = self.head.next
		data = list()
		for _ in range(self.count):
			data.append(current_node.val)
			current_node = current_node.next
		return data
			
# Test

myLinkedList = MyLinkedList()
myLinkedList.addAtHead(7)
myLinkedList.addAtIndex(1,2)
myLinkedList.addAtIndex(2,3)
print(myLinkedList.pprint())
myLinkedList.deleteAtIndex(1)
print(myLinkedList.pprint())
