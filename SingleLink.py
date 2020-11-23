#链表
#元组也可以实现
#python 里等号意味着指向
class Node(object):
	"""docstring for SingleNode"""
	def __init__(self, item):
		self.item = item
		self.next = None # donnot know at the initial
class SingleLink(object):
	"""docstring for SingleNode"""
	#各种方法都是对象方法发 因为是先建立一个对象 再对对象进行操作

	def __init__(self):
		self._head = None  #头节点指向none （私有变量）


	#if we know the first node in our singleLink	
	# def __init__(self,node):
	# 	self._head = node

	def is_empty(self):
		return self._head == None

	def length(self):
		cur = self._head
		count = 0
		while(cur != None):
			count = count + 1
			cur = cur.next
		return count

	def travel(self):
		cur = self._head
		while(cur != None):
			print(cur.item) #不换行
			cur = cur.next
		
	def add(self,item):
		NewNode = Node(item)
		NewNode.next = self._head
		self._head = NewNode

	def append(self,item):
		"""已经把第一个节点赋值到头节点了 注意！！"""
		NewNode = Node(item)
		if self.is_empty():
			self._head = NewNode
		else:
			cur = self._head
			while(cur.next != None):
				cur = cur.next
			cur.next = NewNode
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
		cur = self._head
		if cur.item == item:
			NewNode = Node(item)
			NewNode.next = self._head.next
			self._head = NewNode
		while(cur != None):
			cur = cur.next
			if cur.next.item == item:
				cur.next = cur.next.next
				return 0

				


	def secrch(self, item):
		cur = self._head
		while(cur != None):
			if cur.item == item:
				return True
			cur = cur.next
		return False

singleLink_obj = SingleLink()
# node_obj1 = Node(100)
# singleLink_obj.append(100)
singleLink_obj.append(30)
singleLink_obj.append(40)
singleLink_obj.append(50)
singleLink_obj.add(80)
# singleLink_obj.travel()
singleLink_obj.insert(1,100)
singleLink_obj.remove(50)
singleLink_obj.travel()		
		
