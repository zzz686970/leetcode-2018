class Node(object):
	def __init__(self, val, next):
		self.val = val
		self.next = next

class linkedList(object):
	def __init__(self, iterable=()):
		self.head = None
		self._counter = 0
		if isinstance(iterable, (str, tuple, list)):
			for item in iterable[::-1]:
				self.push(item)

	def push(self, val):
		new_head = Node(val, self.head)
		self.head = new_head
		self._counter += 1

	def pop(self):
		if not self.head:
			raise IndexError("list is empty!")

		output = self.head.val
		self.head = self.head.next
		self._counter -= 1
		return output

	def size(self):
		return self._counter

	def __len__(self):
		return self._counter


	def search(self, val):
		curr = self.head
		while curr:
			if curr.val == val:
				return curr

			curr = curr.next

		return curr

	def remove(self, node):
		curr = self.head

		while curr.next:
			while curr.next == node:
				curr.next = curr.next.next

			curr = curr.next

		return curr

	def display(self):
		st = "("
		curr = self.head

		while curr:
			st += "'{}', ".format(curr.val)
			curr = curr.next
		st = st[:-2] + ")"
		return st


# a_list = [2,3,5,6,8,9]
# newList = LinkedList(a_list)
# a = newList.remove(5)
# print()
# # print(newList.__len__())
