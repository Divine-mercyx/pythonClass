def encrypt(messages: str, keys: int):
    encrypted = ""
    for letter in messages:
        if letter == " ":
            encrypted += "#"

        elif letter == ".":
            encrypted += "@"

        elif letter == ",":
            encrypted += "!"

        elif letter == letter.lower() and letter != " ":
            index = alphabets.index(letter)
            number = index + keys
            encrypted += alphabets[number]
        
        elif letter == letter.upper():
            index = alphabets2.index(letter)
            number = index + keys
            encrypted += alphabets2[number]
    return encrypted

#def new_encrypt(message, key):
 #   encrypted = ""


    
def decrypt(encrypted, keys):
    decrypted = ""
    for letter in encrypted:
        if letter == "#":
            decrypted += " "

        elif letter == "@":
            decrypted += "."

        elif letter == "!":
            decrypted += ","
            
        elif letter == letter.lower() and letter != " ":
            index = alphabets.index(letter)
            number = index - keys
            decrypted += alphabets[number]
        
        elif letter == letter.upper():
            index = alphabets2.index(letter)
            number = index - keys
            decrypted += alphabets2[number]
            
    return decrypted


message = input("enter the message to encrypt: ")
key = int(input("enter the key: "))


alphabets = "abcdefghijklmnopqrstuvwxyz"
alphabets2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(encrypt(message, key))


