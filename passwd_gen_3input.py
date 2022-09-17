#start by importing modules
from sre_parse import SPECIAL_CHARS
import string
import random

#variables to generate password
alphabets = list(string.ascii_letters)
numerals = list(string.digits)
special_char = list("!#$%&_-+@?")
characters = list(alphabets+(list(numerals)+special_char))




#define function
def password_generator():
    #user input number of character
    lenght = int(input("Please enter password lenght: "))

    #user specify character types required
    alphabet_count = int(input("Please enter alphabet count required: "))
    numbers_count = int(input("Please enter digit count required: "))
    specialchar_count = int(input("Please enter special count required: "))

    char_count  = alphabet_count + numbers_count + specialchar_count

    #check the total char input by user char_count
    #print to screen if sum greater than input lenght

    if char_count > lenght:
        print("Character specified is greater that lenght entered")
        return

    #initialize password
    password = []

    #random alphabet selection
    for i in range (alphabet_count):
        password.append(random.choice(alphabets))

    #random numerals selection
    for i in range (numbers_count):
        password.append(random.choice(numerals))

    #random special_char selection
    for i in range (specialchar_count):
        password.append(random.choice(special_char))

    #auto complete charater count when specified character sum < lenght specified
    if char_count < lenght:
        random.shuffle(characters)
        for i in range (lenght - char_count):
            password.append(random.choice(characters))

    #shuffling the resulting passwd
    random.shuffle(password)

    #converting list to string and printing the resulting list
    print("".join(password))
#calling function
password_generator()

 