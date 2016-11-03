def main():
	string = input("Enter string for secret code: ")
	output = ""
	for char in string:
		output = output + str(ord(char)) + " "
	print(output)

main()