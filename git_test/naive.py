def naive_log2(x):
	count = 0
	while x > 1:
		x /= 2
		count += 1
	return count