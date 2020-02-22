from itertools import groupby

def checkhash(seq, f, mod):
	m = sorted([f(x) % mod for x in seq])
	cols = [len(list(group)) for key, group in groupby(m)]
	return (max(cols), min(cols))