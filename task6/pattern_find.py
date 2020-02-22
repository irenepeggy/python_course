s = input()
template = input()

ans= -1

for i in range(len(s) - len(template) + 1):
	for j, t in enumerate(template):
		if not (s[i+j] == t or t == '@'):
			break
	else:
		ans = i
		break

print(ans)