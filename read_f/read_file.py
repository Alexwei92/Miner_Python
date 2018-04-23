def read_file(filename):
	try:
		with open(filename) as f:
			str = f.read()
		if not str:
			sys.exit("\033[1;31;47m Error: File '%s' is empty. \033[0m" %filename)
	except FileNotFoundError as err:
		sys.exit("\033[1;31;47m %s \033[0m" %err)
	else:
		return str