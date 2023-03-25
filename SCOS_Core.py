def load(f):
	file = open(f)
	for f in len(f):
		out = file.readline()
		if out == "exit":
			exit()
		exec(out)

