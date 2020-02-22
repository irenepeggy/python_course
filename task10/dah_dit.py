class morse:


	def __init__(self, *s):
		self.a = []
		
		if (len(s)  == 1):
			s = list(s[0])

		if (len(s) > 0):
			dot = ' ' if ('.' in set(s) or s[len(s) - 1] == ' ') else '.'
		
		s = ''.join(s)
			
		if len(s) == 0:
			self.sep = ','
			self.space = ' '
			self.dah, self.di, self.dit, self.dash = 'dah', 'di', 'dit', '.'
		else:

			s = s.split()
			if len(s) == 1:
				s = list(s[0])
				self.sep = ' '
				self.space = ''
				dot = ' '
			else:
				self.sep = ','
				self.space = ' '
			if len(s) == 2:
				self.dah, self.di, self.dit, self.dash = s[1], s[0], s[0], dot
			elif len(s) == 3:
				self.dah, self.di, self.dit, self.dash = s[2], s[0], s[1], dot
			else:
				self.dah, self.di, self.dit, self.dash = s[2], s[0], s[1], s[3]

	def __neg__(self):

		head = self.dah

		self.a = [head] + self.a
		return self

	def __pos__(self):
		head = ''
		if len(self.a) == 0 or self.a[0] == ',':
			head = self.dit
		else:
			head = self.di

		self.a = [head] + self.a
		return self

	def __invert__(self):
		self.a = [self.sep] + self.a
		return self

	def __str__(self):
		if len(self.a) == 0:
			return '.'
		
		sstr = self.a[0]
		for x in self.a[1:]:	
			if x == self.sep:
				sstr += self.sep 
			else:
				sstr += self.space + x

		if (self.dash == '.' and '.' in {self.di, self.dit, self.dah}):
			return sstr + " "
		else:
			return sstr + self.dash



	

