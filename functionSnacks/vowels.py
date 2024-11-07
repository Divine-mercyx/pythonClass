def vowels(letters):
	vowel = 0
	for letter in letters:
		if letter in ("a", "e", "i", "o", "u"):
			vowel += 1
	return vowel



letters = input("enter a word: ").lower()
print(vowels(letters))