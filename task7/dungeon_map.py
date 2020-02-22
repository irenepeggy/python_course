
s = input().split(' ')
dmap = dict()

while (len(s) == 2):

	if s[0] in dmap:
		dmap[s[0]].add(s[1])
	else:
		dmap[s[0]] = set([s[1]])

	if s[1] in dmap:
		dmap[s[1]].add(s[0])
	else:
		dmap[s[1]] = set([s[0]])

	s = input().split(' ')

start = s[0]
finish = input()

worklist = set([start])
checked = set()
while(len(worklist) > 0):
	nextwork = set()
	checked.update(worklist)

	for v in worklist:
		for fromV in dmap[v]:
			if not fromV in checked:
				nextwork.add(fromV)
				
	worklist.clear()
	worklist.update(nextwork)

print("YES" if finish in checked else "NO")






