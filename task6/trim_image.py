def normalize(tuple):
	splitted = tuple.split(' ')
	rx, ry, rw, rh = [int(c) for c in splitted[:4]]
	c = splitted[4]
	return min(rx, rx + rw), min(ry, ry + rh), abs(rw), abs(rh), c

rects = []
pX, pY, pW, pH = 0, 0, 0, 0
x, y, w, h, c = normalize(input())



while ((x, y, w, h, c) != (0, 0, 0, 0, '0')):
	if (pW == 0 or pH == 0):
		pX, pY, pW, pH = x, y, w, h

	if (w != 0 and h != 0):
		pW = max(x + w, pX + pW) - min(x, pX)
		pH = max(y + h, pY + pH) - min(y, pY)

		pX = min(x, pX)
		pY = min(y, pY)
		
		rects.append([x, y, w, h, c])
	x, y, w, h, c = normalize(input())

picture = [['.' for j in range(pW)] for i in range(pH)]

for x, y, w, h, c in rects:
	for i in range(y, y + h):
		for j in range(x, x + w):
			picture[i - pY][j - pX] = c

for row in picture:
	for j, c in enumerate(row):
		print(c, end='\n' if j == pW-1 else '')

