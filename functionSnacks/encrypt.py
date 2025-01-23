def encrypt_upperText(upper, alphabets, encrypted):
    index = alphabets.index(upper.lower())
    if (26 - index) < 13: encrypted += alphabets[13 - (26 - index)].upper()
    else: encrypted += alphabets[index + 13].upper()
    return encrypted



def encrypt_text(text):
    if type(text) is not str:
        raise TypeError("Text must be of type str")

    encrypted = ""
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for char in text:
        if char.lower() not in alphabets: encrypted += char
        elif char == char.upper(): encrypted = encrypt_upperText(char, alphabets, encrypted)
        else:
            index = alphabets.index(char)
            if (26 - index) < 13: encrypted += alphabets[13 - (26 - index)]
            else: encrypted += alphabets[index + 13]
    return encrypted


