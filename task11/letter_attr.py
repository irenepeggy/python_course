import re

class LetterAttr:

	def __getattr__(self, attr):
		return attr

	def __setattr__(self, attr, value):	
		s = ''
		for c in value:
			s += c if c in attr else ''
		self.__dict__[attr] = s
		

