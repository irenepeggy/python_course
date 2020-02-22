def chainslice(begin, end, *seq):
	i = 0
	for s in seq:
		for x in s:
			if (i >= begin ):
				yield x
			i += 1
			if (i == end):
				break;
		if (i == end):
			break;
