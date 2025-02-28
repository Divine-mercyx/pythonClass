
def validate_name_and_token(name, token):
    if not name: raise ValueError("Name is empty")
    if not token: raise ValueError("Token is empty")

class Player:
    def __init__(self, name, token):
        validate_name_and_token(name, token)
        self.__name = name
        self.__token = token


    def get_name(self):
        return self.__name

    def get_token(self):
        return self.__token
    #
    # def __str__(self):
    #     return f"name: {self.__name}\ntoken: {self.__token}\n"

