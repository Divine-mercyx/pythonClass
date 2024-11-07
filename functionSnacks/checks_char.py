def count_character(word, character):
	count = 0
	for letter in word:
		if character.lower() == letter.lower():
			count += 1
	return count


words = input("input the words: ")
char = input("input the characer: ")

print("output: ", count_character(words, char))
