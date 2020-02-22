def sizer(c):
	class SizedCls(c):
		def __new__(self, value):
			obj = c.__new__(self, value)
			obj._size = -1
			
			return obj

		@property
		def size(self):
			return self._size

		@size.getter
		def size(self):
			if self._size == -1:
				return len(self) if '__len__' in dir(self) else int(self)
			else:
				return self._size

		@size.setter
		def size(self, s):
			self._size = s

		
	return SizedCls



