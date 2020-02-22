
class WeAre:

	_count = 0

	def __init__(self):
		WeAre._count += 1
    
	@property
	def count(self):
		return self._count
	
	@count.setter
	def count(self, v):
		WeAre._count = WeAre._count

	@count.deleter
	def count(self):
		pass

	def __del__(self):
		WeAre._count -= 1
		del self
	

