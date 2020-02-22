def fix(n):
	def fix_decorator(func):
		def newfunc(*args, **kwargs):
			new_args = [round(arg, n) if type(arg) == float else arg for arg in args]
			new_kwargs = dict([(k, round(v, n) if type(v) == float else v) for k, v in kwargs.items()])
			ret = func(*new_args, **new_kwargs)
			return round(ret, n) if type(ret) == float else ret
		return newfunc
	return fix_decorator