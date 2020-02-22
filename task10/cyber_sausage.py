from math import *

class sausage:
	slen = 12


	def __init__(self, staff = 'pork!', v = 1):
		self.staff = staff
		self.v = eval(v) if type(v) == str else v

	def __add__(self, ss):
		return sausage(self.staff, self.v + ss.v)

	def __sub__(self, ss):
		v = self.v - ss.v
		return sausage(self.staff, v if v > 0 else 0) 

	def __mul__(self, x):
		v = self.v * x
		return sausage(self.staff, v if v > 0 else 0) 

	def __rmul__(self, x):
		return self.__mul__(x)

	def __truediv__(self, x):
		v = self.v.__truediv__(x)
		return sausage(self.staff, v if v > 0 else 0) 

	def __bool__(self):
		return False if self.v == 0  or self.staff == '' else True


	def __str__(self):

		def get_line():
			line = ''
			for y in range(self.slen // len(self.staff)):
				line += self.staff
			line += self.staff[:self.slen % len(self.staff)]
			return line

		sstr = ''

		line = get_line()
		length_mod = trunc((self.v % 1) * self.slen)

		if (not self):
			return '/|\n||\n||\n||\n\\|'

		for x in range(trunc(self.v)):
			sstr += '/------------\\'
		if (self.v % 1):
			sstr += '/------------\\'[:length_mod + 1] + '|'
		sstr += '\n'
			

		for n in range(3):
			for x in range(trunc(self.v)):
				sstr += '|' + line + '|'
			if (self.v % 1):
				sstr += '|' + line[:length_mod] + '|'
			
			sstr += '\n'

		for x in range(trunc(self.v)):
			sstr += '\\------------/'
		if (self.v % 1):
			sstr += '\\------------/'[:length_mod + 1] + '|'

		return sstr


