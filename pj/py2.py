r = list(map(chr, range(128)))#range(32, 128 - 1)))
print(f'{r}\n')
i = 0
for elem in r:
	print(f"{i}: {elem.encode()}")
	i+=1