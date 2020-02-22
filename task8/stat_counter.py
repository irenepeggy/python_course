def statcounter():
	d = dict()
	call = yield d
	while call:
		def newfunc(*args, func=call, **kwargs):
			d[func] = d[func] + 1 if func in d.keys() else 1
			return func(*args, **kwargs)
		call = yield newfunc
