s = input().split(' ')

dset = dict()
while (len(s) == 2):
	raw = [{s[0]}, {s[1]}]
	keys = set()
	for k, s in dset.items():
		if raw[0].issubset(s):
			raw[0] = s
			keys.add(k)
		elif raw[1].issubset(s):
			raw[1] = s
			keys.add(k)
	for k in keys:
		dset.pop(k)
	keys.clear()
	newset = raw[0].union(raw[1])
	dset[hash(str(newset))] = newset
	s = input().split(' ')

start = s[0]
finish = input()

for s in dset.values():
	if {start, finish}.issubset(s):
		print('YES')
		break
else:
	print('NO')