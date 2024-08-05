import string
import random

class GeneratePassword():
    def __init__(self, length) -> None:
        if length <= 0:
            raise ValueError("Less than or equal to 0.")
        elif type(length) != int:
            raise TypeError("Not a number.")
        self.lengt = length
    
    def generate(self) -> str:
        symbols = string.ascii_letters + string.hexdigits + string.punctuation
        password = ""
        for _ in range(self.lengt):
            password += random.choice(symbols)
        return password