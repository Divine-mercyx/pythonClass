def acronyms(word):
	acronym = ""
	letters = word.split()
	for letter in letters:
		acronym += letter[0]
	return acronym


words = input("input: ")
print("output: " + acronyms(words))
