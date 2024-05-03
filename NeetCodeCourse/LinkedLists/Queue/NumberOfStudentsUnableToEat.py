from typing import List

class ListNode:
	def __init__(self,val=0,next=None):
		self.val = val
		self.next = next
		
class Solution:
	def __init__(self) -> None:
		self.students_queue = ListNode()
		self.sandwiches_queue = ListNode()

	def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
		for x in students:
			self.appendStudentsQueue(x)
		for y in sandwiches:
			self.appendSandwichedQueue(y)

		loop = 0
		while self.sandwiches_queue.next and self.students_queue.next:
			self.pprint()
			self.pprint(False)
			if self.sandwiches_queue.next.val == self.students_queue.next.val:
				self.dequeueSandwiches()
				self.dequeueStudents()
				loop = 0
			else:
				val = self.dequeueStudents()
				self.enqueueStudents(val)
				loop += 1
			if loop > len(students):
				break
		return self.length()
	
	def length(self):
		len = 0
		current_node = self.sandwiches_queue
		while current_node.next:
			current_node = current_node.next
			len += 1
		return len
	def enqueueStudents(self,val):
		newNode = ListNode(val)
		
		students_queue = self.students_queue.next
		if students_queue:
			while students_queue.next is not None:
				students_queue = students_queue.next
			students_queue.next = newNode
		else:
			self.students_queue = newNode

	def enqueueSandwich(self,val):
		newNode = ListNode(val)
		
		sandwich_queue = self.sandwiches_queue
		while sandwich_queue.next is not None:
			sandwich_queue = sandwich_queue.next
		sandwich_queue.next = newNode

	def dequeueStudents(self):
		if not self.students_queue.next:
			return None
		
		students_head_to_ret = self.students_queue.next
		self.students_queue = self.students_queue.next
		return students_head_to_ret.val
	
	def dequeueSandwiches(self):
		if not self.sandwiches_queue.next:
			return None
		
		sandwiches_queue_head_to_ret = self.sandwiches_queue.next
		self.sandwiches_queue = self.sandwiches_queue.next
		return sandwiches_queue_head_to_ret.val
	
	def appendStudentsQueue(self,student):
		students_queue = self.students_queue
		while students_queue.next is not None:
			students_queue = students_queue.next
		students_queue.next = ListNode(student)
	
	def appendSandwichedQueue(self,sandwich):
		sandwich_queue = self.sandwiches_queue
		while sandwich_queue.next is not None:
			sandwich_queue = sandwich_queue.next
		sandwich_queue.next = ListNode(sandwich)

	def pprint(self,sandwich=True):
		if not sandwich:
			current_node = self.students_queue
		else:
			current_node = self.sandwiches_queue
		node_list = list()
		while current_node.next is not None:
			current_node = current_node.next
			node_list.append(current_node.val)
		print(node_list)
			
x = Solution()
print(x.countStudents([0,0,1,1,0,0,0,0,1,0,0,1,1,0,1,1],[1,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0]))