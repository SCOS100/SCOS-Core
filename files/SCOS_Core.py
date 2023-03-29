def load(f):
	file = open(f)
	while True:
		out = file.readline()
		if out == "exit":
			exit()
		exec(out)
		if out == None:
		  print("Got error: 1")
		  input("Press enter to exit...")
		  exit()

