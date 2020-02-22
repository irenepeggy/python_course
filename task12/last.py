import keyword
import re

d = {}
s = input()
while (not s == '.' and not s == ""):
	if s[0] == '#': 
		s = input()
		continue
	try:
		assign_times = len(re.findall(r'(?==)', s) )
		if assign_times > 1:
			res = f"invalid assignment '{s}'"
		elif assign_times == 1:
			identifier = s[:s.find('=')]
			if keyword.iskeyword(identifier) or not identifier.isidentifier():
				res = f"invalid identifier '{identifier}'"
			else:
				d[identifier] = eval(s[s.find('=')+1:], d)
				s = input()
				continue
		else:
			res = eval(s, d)
	except Exception as e:
		res = e

	print(res)
	s = input()


			

