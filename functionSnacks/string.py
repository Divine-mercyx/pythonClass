def string_palindrome(word):

	reverse = word[::-1]
	if word == reverse:
		return True
	else:
		return False


words = input("input: ")
print("output: ", string_palindrome(words))