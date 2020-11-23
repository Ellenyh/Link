#单向循环列表

class Node(object):
	"""docstring for SingleNode"""
	def __init__(self, item):
		self.item = item
		self.next = None # donnot know at the initial
class SingleCycleLink(object):

	def __init__(self):
		self._head = None  #头节点指向none （私有变量）

	def is_empty(self):
		return self._head == None

	def length(self):
		if self._head == None:
			return 0
		cur = self._head
		count = 1
		while(cur.next != self._head):
			count = count + 1
			cur = cur.next
		return count

	def travel(self):
		if self.is_empty():
			return 0
		cur = self._head
		while(cur.next != self._head):
			print(cur.item) #不换行
			cur = cur.next
		print(cur.item)
		
	def add(self,item):
		NewNode = Node(item)
		if self._head == None:
			self._head = NewNode
			NewNode.next = NewNode
		else:
			cur = self._head
			while(cur.next != self._head):
				cur = cur.next
			NewNode.next = self._head
			self._head = NewNode
			cur.next = self._head

	def append(self,item):
		"""已经把第一个节点赋值到头节点了 注意！！"""
		NewNode = Node(item)
		if self.is_empty():
			self._head = NewNode
			NewNode.next = NewNode
		else:
			cur = self._head
			while(cur.next != self._head):
				cur = cur.next
			cur.next = NewNode
			NewNode.next = self._head
		return self

	def insert(self, pos, item):
		#指定位置添加 pos from 0
		cur = self._head
		if pos == 0:
			self.add(item)
		elif pos > self.length():
			self.append(item)
		else:
			count = 0
			while(count != pos-1):
				count = count + 1
				cur = cur.next
			NewNode = Node(item)
			NewNode.next = cur.next
			cur.next = NewNode

	def remove(self, item):
		if self.is_empty():
			return 0
		cur = self._head
		pre = None
		flag = self._head
		while(cur.next != self._head):
			if cur.item == item:
				if cur == self._head:
					while(flag.next != self._head):
						flag = flag.next
					self._head = cur.next
					flag.next = self._head

				else:
					pre.next = cur.next
			pre = cur
			cur = cur.next
		if cur.item is item:
			if cur is self._head:
				self._head = None
			else:
				pre.next = cur.next

	def secrch(self, item):
		if self.is_empty():
			return False
		cur = self._head
		while(cur.next != self._head):
			if cur.item == item:
				return True
			cur = cur.next
		if cur.item is item:
			return True
		return False

singleLink_obj = SingleCycleLink()
# node_obj1 = Node(100)
# singleLink_obj.append(100)
singleLink_obj.append(30)
singleLink_obj.append(40)
singleLink_obj.append(50)
singleLink_obj.add(80)
# # singleLink_obj.travel()
singleLink_obj.insert(1,100)
singleLink_obj.remove(30)
singleLink_obj.travel()		
		