class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def fromvalues(Cls, values):
        head = None
        for value in reversed(values):
            head = Cls(value, head)
        return head

    def __iter__(self):
        yield self.val
        if self.next:
            yield from self.next

    def __str__(self):
        return "->".join(map(str, self))