class stack:

	def __init__(self):
		self.arr=[]
	def isEmpty(self):
		return self.arr.size() == 0
	def push(self,item):
		self.arr.append(item)
	def pop(self):
		return self.arr.pop()
	def size(self):
		return len(self.arr)
		
		
