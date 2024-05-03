class ListNode:
	def __init__(self,val='',next=None,prev=None):
		self.val = val
		self.next = next
		self.prev = prev

class BrowserHistory:

	def __init__(self, homepage: str):
		self.back_history = ListNode(homepage,None,None)

	def visit(self, url: str) -> None:
		self.back_history.next = ListNode(url,None,self.back_history)
		self.back_history = self.back_history.next

	def back(self, steps: int) -> str:
		while self.back_history.prev and steps > 0 :
			self.back_history = self.back_history.prev
			steps -=1
		return self.back_history.val

	def forward(self, steps: int) -> str:
		while self.back_history.next and steps > 0 :
			self.back_history = self.back_history.next
			steps -=1
		return self.back_history.val

x = BrowserHistory('zav.com')
x.visit('kni.com')
print(x.back(7))
print(x.back(7))
print(x.forward(5))
print(x.back(1))
print(x.forward(1))
x.visit('pwrrbnw.com')
x.visit('mosohif.com')
print(x.back(9))