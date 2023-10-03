def uppercase(str):
	for i in range(len(str)):
		uppercase_char = chr(ord(str[i]) - 32)
		print("{}".format(uppercase_char), end="")
	print()
