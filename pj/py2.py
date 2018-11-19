f = lambda x,n: x**3 % n
def main():
	n = 7870
	while True:
		for x in range(10000):
			if f(x, n) == 5713 and f(x + 1, n) == 5783:
				for y in range(10000):
					if f(y, n) == 7821 and f(y + 1, n) == 7870:
						print('x:{}, y:{}, n:{}, success'.format(x,y,n))
						return
		n+=1
		
if __name__ == '__main__':
	main()