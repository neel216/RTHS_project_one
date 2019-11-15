class Math:
	addition(self, foo, bar):
		try:
			fizz = int(foo)
			bizz = int(bar)
		except ValueError:
			print('Could not convert numbers while adding.')
			return 0
		return (foo).__add__(bar)
	subtraction(self, foo, bar):
		try:
			fizz = int(foo)
			bizz = int(bar)
		except ValueError:
			print('Could not convert numbers while adding.')
			return 0
		return (foo).__sub__(bar)
	multiplication(self, foo, bar):
		try:
			fizz = int(foo)
			bizz = int(bar)
		except ValueError:
			print('Could not convert numbers while adding.')
			return 0
		return (foo).__mul__(bar)

if __name__ == '__main__':
	math = Math()
	print(math.addition(1, 1))
	print(math.subtraction(1, 1))
	print(math.multiplication(1, 2))
