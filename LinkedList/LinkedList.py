class Node():
  def __init__(self, data = None): 
    self.data = data
    self.next = None

class LinkedList():
	def __init__(self):  
		self.head = Node()
    
	def append(self,data):
		new_node = Node(data)
		current_node = self.head
		while current_node.next is not None:
			current_node = current_node.next
		current_node.next = new_node
    
	def length(self):
		current_node = self.head
		counter = 0
		while current_node.next is not None:
			counter += 1
			current_node = current_node.next
		return counter

	def pprint(self):
		current_node = self.head
		node_list = list()
		while current_node.next is not None:
			current_node = current_node.next
			node_list.append(current_node.data)
		print(node_list)
	
	def get(self,index):
		if index > self.length():
			return "Index out of range"
		current_node = self.head
		current_index = 0
		while True:
			if index == current_index:
				return current_node.data
			current_index += 1
			current_node = current_node.next
	
	def addAtHead(self, data: int) -> None:
		self.addAtIndex(0,data)
		
	def addAtTail(self, val: int) -> None:
		self.addAtIndex(self.length(),val)

	def addAtIndex(self, index: int, val: int) -> None:
		if index > self.length():
			return "Index out of range"
		current_node = self.head
		current_index = 0
		prev_node = Node()
		if index != self.length():
			while current_node.next is not None:	
				prev_node = current_node
				current_node = current_node.next
				if index == current_index:
					new_node = Node(val)
					prev_node.next = new_node
					new_node.next = current_node
					break
				current_index += 1
		else:
			while True:
				if current_node.next is None:
					new_node = Node(val)
					current_node.next = new_node
					break
				current_node = current_node.next

	def deleteAtIndex(self, index: int) -> None:
		if index > self.length():
			return "Index out of range"
		current_node = self.head
		current_index = 0
		prev_node = None
		while current_node.next is not None:
			print(current_node.data)
			prev_node = current_node
			current_node = current_node.next
			if index == current_index:
				prev_node.next = current_node.next
				break
			current_index += 1
		


						

linkedList = LinkedList()
linkedList.addAtHead(7)
linkedList.addAtHead(2)
linkedList.addAtHead(1)
linkedList.addAtIndex(3,0)
print(linkedList.length())
linkedList.pprint()