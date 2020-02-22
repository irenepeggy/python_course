import operator

inp = input().split(' ')

i = 0
d=dict()
maxk=[]
maxv=0

while(len(inp) == 4):
	x1, y1, z1, n1 = [eval(inp[0]), eval(inp[1]), eval(inp[2]), inp[3]]	
	d[i] = dict(zip("xyzn", [x1, y1, z1, n1]))
	for j in range(i):
		x2, y2, z2, n2 = d[j].values()
		v = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**(0.5)
		if v > maxv: 
			maxk=[n1, n2]
			maxv=v

	i += 1
	inp = input().split(' ')


print(" ".join(sorted(maxk)))