seglist = sorted(eval(input()))

total_sum = 0
acc_seg = (0, 0)

for seg in seglist:
	if acc_seg[1] < seg[0]:
		total_sum += acc_seg[1] - acc_seg[0]
		acc_seg = seg
	elif acc_seg[1] < seg[1]:
		acc_seg = (acc_seg[0], seg[1])
		
total_sum += acc_seg[1] - acc_seg[0]
print(total_sum)