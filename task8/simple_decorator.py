def nonify(func):
	def newfunc(*args, **kwargs):
		ret = func(*args, **kwargs)
		return ret if ret else None
	return newfunc

