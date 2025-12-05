import random
import string
from abc import ABC, abstractmethod

import nltk

nltk.download('words')

class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass
    
    
class PinGenerator(PasswordGenerator):
    def __init__(self, length: int):
        self.length = length
    
    def generate(self) -> str:
        return ''.join([random.choice(string.digits) for _ in range(self.length)])
    

class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation
        
    def generate(self) -> str:
        return ''.join([random.choice(self.characters) for _ in range(self.length)])

    
class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
            self,
            number_of_words: int = 4, 
            seperator: str  = '-', 
            capitalize: bool = False, 
            vocabulary: list = None 
    ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()
            
        self.number_of_words = number_of_words
        self.capitalize = capitalize
        self.seperator = seperator
        self.vocabulary = vocabulary
        
    def generate(self) -> str:
        password_words = [random.choice(self.vocabulary) for _ in range(self.number_of_words)]
        if self.capitalize:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]
            
        return self.seperator.join(password_words)
         
if __name__ == '__main__':
    # password_generator = PinGenerator(length=10)
    # print(password_generator.generate())
    
    password_generator = RandomPasswordGenerator(length=30, include_numbers= False, include_symbols= False)
    print(password_generator.generate())
    
    # password_generator = MemorablePasswordGenerator(number_of_words=4,seperator='-',capitalize=True)
    # print(password_generator.generate())