import string
import random

class GeneratePassword():
    def __init__(self) -> None:
        self.length = 12
    
    def generate(self, output_text) -> None:
        output_text.configure(state="normal")
        symbols = string.ascii_letters + string.hexdigits + string.punctuation
        password = ""
        for _ in range(self.length):
            password += random.choice(symbols)
        output_text.insert(index="1.0 ",text=f'{password}\n')
        output_text.configure(state="disabled")