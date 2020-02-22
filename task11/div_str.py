class DivStr(str):

	def div_str(f):
		def div_str_f(*args, **kwargs):
			res = f(*args, **kwargs)
			return DivStr(res) if type(res) == str else res
		return div_str_f

	def __new__(self, *args, **kwargs):
		

		obj = str.__new__(self, *args, **kwargs)

		for key, value in str.__dict__.items():
			if key != '__new__' and hasattr(value, '__call__'):
				setattr(self, key, self.div_str(value))
		return obj


	def __str__(self, *args, **kwargs):
		return super().__str__(*args, **kwargs)

	def __truediv__(self, n):
		return DivStr(self[:len(self)//n])

	def __floordiv__(self, n):
		return DivStr(self[:len(self)//n])
