def xehs(s):
	ns = [ord(x)-32 for x in s]
	ns.reverse()
	i = 1
	res = 0
	for x in ns:
		res += x * i
		i *= 64
	return res

def shex(n):
	res = ""
	while n:
		res = chr(n % 64 + 32) + res
		n //= 64
	return res

def encode(txt): 
	d = {}
	for c in txt:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1

	val = '0'
	encodict = {}
	for k, v in sorted(d.items(), key=lambda item: (-item[1], -ord(item[0]))):
		encodict[k] = val
		val = '1' + val
		
	bitencoding = "".join([encodict[k] for k in txt]) 
	nulls = 0 if len(bitencoding) % 6 == 0 else 6 - len(bitencoding) % 6
	bitencoding += "0" * nulls
	encoded ="".join([chr(eval("0b"+bitencoding[i*6:i*6+6]) + 32)  for i in range(len(bitencoding)//6)])

	return (len(txt), "".join(encodict.keys()), encoded)


def decode(length, chars, code): 
	def getbits(c):
		b = str(bin(ord(c) - 32))[2:]
		return "0"*(6-len(b)) + b

	val = '0'
	decodict = {}
	for k in chars:
		decodict[val] = k
		val = '1' + val
	
	bitencoding = "".join([getbits(c) for c in code])
	txt, start, i = "", 0, 0
	while i < length:
		end = bitencoding.find('0', start) + 1
		txt += decodict[bitencoding[start:end]]
		start = end
		i += 1

	return txt
