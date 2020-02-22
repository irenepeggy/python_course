from math import *
n, m = eval(input())

n_len = len(str(n))
mult_len = len(str(n*n))
#first_len =max([len(str(col_number * k)) for k in range(block_row_number)])

expr_len = n_len + 3 + n_len + 3 + mult_len
col_len = 1 + 1 + expr_len + 1 #'|', space, expression, space
col_number = 1 + (m - col_len + 2)//col_len

format_str = '{:>{nl}} * {:<{nl}} = {:<{multl}}'

block_row_number = ceil(n / col_number)


# over rows of blocks
for k in range(block_row_number):
	base_n = col_number * k
	print('{:=^{m}}'.format('=', m=m))
	#over rows in each block
	for i in range(n):

		#over cols in each row
		for j in range(col_number):	
			if base_n + j == n:
				break
			end =' | ' if (j != col_number - 1 and base_n + j + 1!= n) else '\n'
			print(format_str.format(base_n + j + 1, i + 1, (base_n + j + 1) * (i+1), nl=n_len, multl=mult_len), end=end)
print('{:=^{m}}'.format('=', m=m))
