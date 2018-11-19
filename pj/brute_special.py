import hashlib
import itertools
import sys
import threading
from time import sleep
try:
	import thread
except ImportError:
	import _thread as thread



#функция-декоратор для управления временем выполнения функций 
def quit_function(func):
	print('{0} TimeoutError'.format(func), file = sys.stderr)
	sys.stderr.flush()
	thread.interrupt_main()

def exit_after(s):
	def outer(fn):
		def inner(*args, **kwargs):
			timer = threading.Timer(s, quit_function, args = [fn.__name__])
			timer.start()
			try:
				result = fn(*args, **kwargs)
			finally:
				timer.cancel()
			return result
		return inner
	return outer
#end

class Password():
	def __init__(self, hash):
		self.hash = hash


	#@exit_after(100)
	def brute(self):
		i = 0
		r = range(10)
		while True:
			i+=1
			combo = itertools.product(r, repeat=i)
			for elem in combo: #перебираем комбинации
				pass_ = ''
				for el in elem: #Делаем строки из комбинаций
					pass_+=str(el) #hashlib.md5(pass_.encode()).hexdigest():
				if hashlib.md5(hex(int(pass_)).encode()).hexdigest() == self.hash: #Сравниваем переданныйй хэш и хэш полученный
					#self.hpass = pass_
					return hex(int(pass_))
			
def main():
	password = '7098d03d3436384f91d662b4f237c0dc'#hex(255255) #type your password here
	print('original: {}'.format(password))
	a = Password(password)
	print('hashed original: {}, \nbruted: {}'.format(a.hash, a.brute()))



if __name__ == '__main__':
	main()

