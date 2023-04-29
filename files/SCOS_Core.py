def load(f):
	file = open(f)
	while True:
		out = file.readline()
		if out == "exit":
			exit()
		if out == None:
		  print("Got error: 1")
		  input("Press enter to exit...")
		  exit()
print("SCOS Core Version 1.0b")
exit()
