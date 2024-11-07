def acronyms(word):
	acronym = ""
	for letter in word:
		if letter == letter.upper() :
			acronym += letter.strip()
	return acronym


words = input("input: ")
print("output: " + acronyms(words))
